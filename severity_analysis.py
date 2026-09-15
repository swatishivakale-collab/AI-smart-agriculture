import cv2
import numpy as np
from pathlib import Path


# =========================
# CONFIGURATION
# =========================

IMAGE_PATH = Path("test_leaf.jpg")

# Yellow/chlorotic tissue contributes only 50%
YELLOW_WEIGHT = 0.5


# =========================
# LOAD IMAGE
# =========================

image = cv2.imread(str(IMAGE_PATH))

if image is None:
    raise FileNotFoundError(f"Could not find image: {IMAGE_PATH}")

image = cv2.resize(image, (500, 500))

print("Image loaded successfully!")


# =========================
# LEAF SEGMENTATION
# =========================

mask = np.zeros(image.shape[:2], np.uint8)

background_model = np.zeros((1, 65), np.float64)
foreground_model = np.zeros((1, 65), np.float64)

rect = (15, 15, 470, 470)

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
    (mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD),
    255,
    0
).astype("uint8")


# =========================
# KEEP LARGEST OBJECT
# =========================

num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
    leaf_mask,
    connectivity=8
)

if num_labels > 1:

    largest_label = 1 + np.argmax(
        stats[1:, cv2.CC_STAT_AREA]
    )

    leaf_mask = np.where(
        labels == largest_label,
        255,
        0
    ).astype("uint8")


# =========================
# CLEAN LEAF MASK
# =========================

kernel = np.ones((5, 5), np.uint8)

leaf_mask = cv2.morphologyEx(
    leaf_mask,
    cv2.MORPH_CLOSE,
    kernel,
    iterations=2
)


# =========================
# INNER LEAF REGION
# =========================

erosion_kernel = np.ones((9, 9), np.uint8)

inner_leaf_mask = cv2.erode(
    leaf_mask,
    erosion_kernel,
    iterations=2
)


# =========================
# HSV IMAGE
# =========================

hsv = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2HSV
)


# =========================
# HEALTHY GREEN
# =========================

lower_green = np.array([36, 35, 30])
upper_green = np.array([95, 255, 255])

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
# YELLOW / CHLOROTIC
# =========================

lower_yellow = np.array([15, 45, 60])
upper_yellow = np.array([35, 255, 255])

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
# REMOVE OVERLAP
# =========================

# Yellow must NOT also be counted as full damage.

not_yellow = cv2.bitwise_not(yellow_mask)


# =========================
# NON-GREEN TISSUE
# =========================

non_green_mask = cv2.subtract(
    inner_leaf_mask,
    healthy_mask
)


# =========================
# FULL DAMAGE
# =========================

# Brown / dark / abnormal non-green tissue,
# excluding yellow tissue.

full_damage_mask = cv2.bitwise_and(
    non_green_mask,
    not_yellow
)


# =========================
# CLEAN MASKS
# =========================

small_kernel = np.ones((3, 3), np.uint8)

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
    yellow_pixels * YELLOW_WEIGHT
)

weighted_damage_pixels = (
    full_damage_pixels
    + weighted_yellow_pixels
)


# =========================
# AFFECTED PERCENTAGE
# =========================

if leaf_pixels > 0:

    affected_percentage = (
        weighted_damage_pixels
        / leaf_pixels
    ) * 100

else:

    affected_percentage = 0.0


# Prevent accidental values above 100%
affected_percentage = min(
    affected_percentage,
    100.0
)


# =========================
# PROTOTYPE SEVERITY
# =========================

if affected_percentage < 10:

    severity = "VERY LOW"

elif affected_percentage < 20:

    severity = "LOW"

elif affected_percentage < 60:

    severity = "MODERATE"

else:

    severity = "HIGH"


# =========================
# OVERLAY
# =========================

overlay = image.copy()

# Yellow/orange visualization
yellow_layer = np.zeros_like(image)
yellow_layer[:, :] = (0, 165, 255)

yellow_area = cv2.bitwise_and(
    yellow_layer,
    yellow_layer,
    mask=yellow_mask
)

# Red visualization for full damage
red_layer = np.zeros_like(image)
red_layer[:, :] = (0, 0, 255)

red_area = cv2.bitwise_and(
    red_layer,
    red_layer,
    mask=full_damage_mask
)

overlay = cv2.addWeighted(
    overlay,
    1.0,
    yellow_area,
    0.45,
    0
)

overlay = cv2.addWeighted(
    overlay,
    1.0,
    red_area,
    0.55,
    0
)

overlay = cv2.bitwise_and(
    overlay,
    overlay,
    mask=leaf_mask
)


# =========================
# PRINT RESULTS
# =========================

print("\n================================")
print("WEIGHTED LEAF SEVERITY ANALYSIS")
print("================================")

print(f"Leaf pixels: {leaf_pixels}")
print(f"Yellow pixels: {yellow_pixels}")
print(f"Full damage pixels: {full_damage_pixels}")

print(
    f"Weighted yellow pixels: "
    f"{weighted_yellow_pixels:.1f}"
)

print(
    f"Weighted damaged pixels: "
    f"{weighted_damage_pixels:.1f}"
)

print(
    f"Estimated affected area: "
    f"{affected_percentage:.2f}%"
)

print(f"Severity level: {severity}")

print("================================")

print(
    "\nYellow/orange area = 0.5 damage weight"
)

print(
    "Red area = 1.0 damage weight"
)


# =========================
# DISPLAY
# =========================

cv2.imshow(
    "Original Image",
    image
)

cv2.imshow(
    "Leaf Mask",
    leaf_mask
)

cv2.imshow(
    "Yellow Tissue - Weight 0.5",
    yellow_mask
)

cv2.imshow(
    "Full Damage - Weight 1.0",
    full_damage_mask
)

cv2.imshow(
    "Weighted Damage Overlay",
    overlay
)

print("\nPress any key on an image window to close.")

cv2.waitKey(0)
cv2.destroyAllWindows()