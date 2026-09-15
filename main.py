from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

import tensorflow as tf
import numpy as np
import cv2

from PIL import Image

from backend.treatments import get_treatment
from backend.disease_info import DISEASE_INFO


# =========================
# FASTAPI APP
# =========================

app = FastAPI(
    title="Tomato Disease Detection API"
)


# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# UPLOAD FOLDER
# =========================

UPLOAD_DIR = Path("backend/uploads")

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# =========================
# AI MODEL
# =========================

MODEL_PATH = Path(
    "ai_model/tomato_disease_model.keras"
)

CLASS_NAMES = [
    "Bacterial_Spot",
    "Early_Blight",
    "Healthy",
    "Late_Blight",
    "Leaf_Mold",
    "Septoria_Leaf_Spot"
]

print("Loading AI model...")

model = tf.keras.models.load_model(
    MODEL_PATH
)

print("AI model loaded successfully!")


# ============================================================
# AFFECTED AREA ANALYSIS
# ============================================================

def calculate_affected_area(image_path):

    image = cv2.imread(
        str(image_path)
    )

    if image is None:
        return 0.0

    image = cv2.resize(
        image,
        (500, 500)
    )


    # =========================
    # LEAF SEGMENTATION
    # =========================

    mask = np.zeros(
        image.shape[:2],
        np.uint8
    )

    background_model = np.zeros(
        (1, 65),
        np.float64
    )

    foreground_model = np.zeros(
        (1, 65),
        np.float64
    )

    rect = (
        15,
        15,
        470,
        470
    )

    cv2.grabCut(
        image,
        mask,
        rect,
        background_model,
        foreground_model,
        8,
        cv2.GC_INIT_WITH_RECT
    )


    leaf_mask = np.where(
        (
            (mask == cv2.GC_FGD)
            |
            (mask == cv2.GC_PR_FGD)
        ),
        255,
        0
    ).astype("uint8")


    # =========================
    # KEEP LARGEST OBJECT
    # =========================

    num_labels, labels, stats, _ = (
        cv2.connectedComponentsWithStats(
            leaf_mask,
            connectivity=8
        )
    )

    if num_labels > 1:

        largest_label = (
            1
            +
            np.argmax(
                stats[
                    1:,
                    cv2.CC_STAT_AREA
                ]
            )
        )

        leaf_mask = np.where(
            labels == largest_label,
            255,
            0
        ).astype("uint8")


    # =========================
    # CLEAN LEAF MASK
    # =========================

    kernel = np.ones(
        (5, 5),
        np.uint8
    )

    leaf_mask = cv2.morphologyEx(
        leaf_mask,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=2
    )


    # =========================
    # INNER LEAF
    # =========================

    erosion_kernel = np.ones(
        (9, 9),
        np.uint8
    )

    inner_leaf_mask = cv2.erode(
        leaf_mask,
        erosion_kernel,
        iterations=2
    )


    # =========================
    # HSV
    # =========================

    hsv = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2HSV
    )


    # =========================
    # HEALTHY GREEN
    # =========================

    lower_green = np.array(
        [36, 35, 30]
    )

    upper_green = np.array(
        [95, 255, 255]
    )

    healthy_mask = cv2.inRange(
        hsv,
        lower_green,
        upper_green
    )

    healthy_mask = cv2.bitwise_and(
        healthy_mask,
        inner_leaf_mask
    )


    # =========================
    # YELLOW TISSUE
    # WEIGHT = 0.5
    # =========================

    lower_yellow = np.array(
        [15, 45, 60]
    )

    upper_yellow = np.array(
        [35, 255, 255]
    )

    yellow_mask = cv2.inRange(
        hsv,
        lower_yellow,
        upper_yellow
    )

    yellow_mask = cv2.bitwise_and(
        yellow_mask,
        inner_leaf_mask
    )


    # =========================
    # NON-GREEN
    # =========================

    non_green_mask = cv2.subtract(
        inner_leaf_mask,
        healthy_mask
    )


    # =========================
    # FULL DAMAGE
    # =========================

    not_yellow = cv2.bitwise_not(
        yellow_mask
    )

    full_damage_mask = cv2.bitwise_and(
        non_green_mask,
        not_yellow
    )


    # =========================
    # CLEAN MASKS
    # =========================

    small_kernel = np.ones(
        (3, 3),
        np.uint8
    )

    yellow_mask = cv2.morphologyEx(
        yellow_mask,
        cv2.MORPH_OPEN,
        small_kernel
    )

    yellow_mask = cv2.morphologyEx(
        yellow_mask,
        cv2.MORPH_CLOSE,
        small_kernel
    )

    full_damage_mask = cv2.morphologyEx(
        full_damage_mask,
        cv2.MORPH_OPEN,
        small_kernel
    )

    full_damage_mask = cv2.morphologyEx(
        full_damage_mask,
        cv2.MORPH_CLOSE,
        small_kernel
    )


    # =========================
    # PIXEL COUNTS
    # =========================

    leaf_pixels = cv2.countNonZero(
        inner_leaf_mask
    )

    yellow_pixels = cv2.countNonZero(
        yellow_mask
    )

    full_damage_pixels = cv2.countNonZero(
        full_damage_mask
    )


    # =========================
    # WEIGHTED DAMAGE
    # =========================

    weighted_yellow_pixels = (
        yellow_pixels * 0.5
    )

    weighted_damage_pixels = (
        full_damage_pixels
        +
        weighted_yellow_pixels
    )


    # =========================
    # CALCULATE %
    # =========================

    if leaf_pixels == 0:
        return 0.0

    affected_percentage = (
        weighted_damage_pixels
        /
        leaf_pixels
    ) * 100

    affected_percentage = max(
        0.0,
        min(
            affected_percentage,
            100.0
        )
    )

    return round(
        affected_percentage,
        2
    )


# ============================================================
# FARMER ALERT INFORMATION
# ============================================================

def get_farmer_info(
    predicted_class,
    severity,
    confidence
):

    # =========================
    # LOW CONFIDENCE
    # =========================

    if confidence < 60:

        return {
            "available": False,
            "reason": "LOW_CONFIDENCE"
        }


    disease_data = DISEASE_INFO.get(
        predicted_class
    )

    if disease_data is None:

        return {
            "available": False,
            "reason": "DISEASE_INFO_NOT_FOUND"
        }


    farmer_info = {}


    for language in [
        "en",
        "hi"
    ]:

        info = disease_data.get(
            language,
            {}
        )


        # =========================
        # HEALTHY
        # =========================

        if predicted_class == "Healthy":

            farmer_info[
                language
            ] = {

                "disease_name":
                    info.get(
                        "disease_name"
                    ),

                "alert_title":
                    info.get(
                        "alert_title"
                    ),

                "message":
                    info.get(
                        "message"
                    ),

                "actions":
                    info.get(
                        "actions",
                        []
                    ),

                "treatment":
                    info.get(
                        "treatment"
                    ),

                "warning":
                    info.get(
                        "warning"
                    ),

                "sprays": []
            }

            continue


        # =========================
        # DISEASE
        # =========================

        language_result = {

            "disease_name":
                info.get(
                    "disease_name"
                ),

            "alert_title":
                info.get(
                    "alert_title"
                ),

            "about":
                info.get(
                    "about",
                    {}
                ),

            "actions":
                info.get(
                    "actions",
                    []
                ),

            "message": None,

            "sprays": [],

            "additional_action": None,

            "warning":
                info.get(
                    "warning"
                )
        }


        # =========================
        # LOW
        # =========================

        if severity == "LOW":

            language_result[
                "message"
            ] = info.get(
                "low_message"
            )


        # =========================
        # MODERATE
        # =========================

        elif severity == "MODERATE":

            language_result[
                "sprays"
            ] = info.get(
                "moderate_sprays",
                []
            )


        # =========================
        # HIGH
        # =========================

        elif severity == "HIGH":

            language_result[
                "sprays"
            ] = info.get(
                "high_sprays",
                []
            )

            language_result[
                "additional_action"
            ] = info.get(
                "high_action"
            )


        farmer_info[
            language
        ] = language_result


    return {
        "available": True,
        "languages": farmer_info
    }


# =========================
# HOME
# =========================

@app.get("/")
def home():

    return {
        "message":
            "Tomato Disease Detection API is running!"
    }


# =========================
# IMAGE UPLOAD + AI
# =========================

@app.post("/upload")
async def upload_image(
    file: UploadFile = File(...)
):

    allowed_types = [
        "image/jpeg",
        "image/png"
    ]


    # =========================
    # FILE VALIDATION
    # =========================

    if file.content_type not in allowed_types:

        return {
            "error":
                "Only JPG, JPEG and PNG images are allowed."
        }


    # =========================
    # SAVE IMAGE
    # =========================

    file_path = (
        UPLOAD_DIR
        /
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )


    # =========================
    # PREPROCESS IMAGE
    # =========================

    image = Image.open(
        file_path
    ).convert("RGB")

    image = image.resize(
        (224, 224)
    )

    image_array = np.array(
        image,
        dtype=np.float32
    )

    image_array = np.expand_dims(
        image_array,
        axis=0
    )


    # =========================
    # AI PREDICTION
    # =========================

    predictions = model.predict(
        image_array,
        verbose=0
    )

    predicted_index = int(
        np.argmax(
            predictions[0]
        )
    )

    predicted_class = (
        CLASS_NAMES[
            predicted_index
        ]
    )

    confidence = (
        float(
            predictions[0][
                predicted_index
            ]
        )
        * 100
    )


    # =========================
    # AFFECTED AREA
    # =========================

    affected_percentage = (
        calculate_affected_area(
            file_path
        )
    )


    # =========================
    # SEVERITY
    # =========================

    severity_result = get_treatment(
        predicted_class,
        affected_percentage
    )

    severity = severity_result[
        "severity"
    ]


    # =========================
    # STATUS
    # =========================

    if confidence < 60:

        status = "UNCERTAIN"

        alert = (
            "Prediction confidence is low. "
            "Please capture a clearer leaf image."
        )


    elif predicted_class == "Healthy":

        status = "HEALTHY"

        alert = (
            "The tomato leaf appears healthy. "
            "Continue regular monitoring."
        )


    elif affected_percentage < 10:

        status = "LOW VISIBLE DAMAGE"

        disease_name = (
            predicted_class.replace(
                "_",
                " "
            )
        )

        alert = (
            f"{disease_name} was detected, "
            f"but estimated visible affected area "
            f"is only {affected_percentage}%. "
            f"Continue monitoring."
        )


    else:

        status = "DISEASE DETECTED"

        disease_name = (
            predicted_class.replace(
                "_",
                " "
            )
        )

        alert = (
            f"{disease_name} detected. "
            f"Estimated visible affected area: "
            f"{affected_percentage}%. "
            f"Please inspect the affected plant."
        )


    # =========================
    # FARMER INFO
    # =========================

    farmer_info = get_farmer_info(
        predicted_class,
        severity,
        confidence
    )


    # =========================
    # FINAL RESPONSE
    # =========================

    return {

        "filename":
            file.filename,

        "content_type":
            file.content_type,

        "prediction":
            predicted_class,

        "confidence":
            round(
                confidence,
                2
            ),

        "affected_area_percent":
            affected_percentage,

        "health_score_percent":
            round(
                max(
                    0.0,
                    100.0 - affected_percentage
                ),
                2
            ),

        "severity":
            severity,

        "status":
            status,

        "alert":
            alert,

        "farmer_info":
            farmer_info,

        "message":
            "Image analyzed successfully!"
    }