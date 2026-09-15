import os
import shutil
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import image_dataset_from_directory

# =========================
# SETTINGS
# =========================

MODEL_PATH = "ai_model/tomato_disease_model.keras"
TEST_DIR = "dataset_split/test"
OUTPUT_DIR = "error_analysis"

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

CLASS_NAMES = [
    "Bacterial_Spot",
    "Early_Blight",
    "Healthy",
    "Late_Blight",
    "Leaf_Mold",
    "Septoria_Leaf_Spot"
]

# =========================
# LOAD MODEL
# =========================

print("Loading model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Model loaded successfully!")

# =========================
# LOAD TEST DATA
# =========================

test_ds = image_dataset_from_directory(
    TEST_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

# =========================
# CREATE OUTPUT FOLDER
# =========================

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# FIND MISCLASSIFIED
# EARLY BLIGHT IMAGES
# =========================

print("\nFinding Early Blight mistakes...")

wrong_count = 0
total_early_blight = 0

for images, labels in test_ds:

    predictions = model.predict(images, verbose=0)

    predicted_labels = np.argmax(predictions, axis=1)

    for i in range(len(labels)):

        actual = labels[i].numpy()
        predicted = predicted_labels[i]

        # Only inspect actual Early Blight
        if actual == 1:

            total_early_blight += 1

            if predicted != actual:

                wrong_count += 1

                # Get original filename
                batch_index = wrong_count

                filename = f"EarlyBlight_WRONG_{batch_index}_Predicted_{CLASS_NAMES[predicted]}.jpg"

                output_path = os.path.join(
                    OUTPUT_DIR,
                    filename
                )

                # Save image
                image = images[i].numpy().astype("uint8")

                tf.keras.utils.save_img(
                    output_path,
                    image
                )

print("\n==============================")
print("EARLY BLIGHT ERROR ANALYSIS")
print("==============================")

print(f"Total Early Blight test images: {total_early_blight}")
print(f"Misclassified Early Blight images: {wrong_count}")

print("\nImages saved to:")
print(OUTPUT_DIR)

print("\nAnalysis completed successfully!")