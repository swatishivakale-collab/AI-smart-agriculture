from pathlib import Path
import random
import shutil

# Original dataset
SOURCE_DIR = Path("dataset")

# New split dataset
OUTPUT_DIR = Path("dataset_split")

# Split ratios
TRAIN_RATIO = 0.80
VAL_RATIO = 0.10
TEST_RATIO = 0.10

# Make results reproducible
random.seed(42)

# Image extensions we accept
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}

# Check ratios
assert TRAIN_RATIO + VAL_RATIO + TEST_RATIO == 1.0

# Check source dataset
if not SOURCE_DIR.exists():
    raise FileNotFoundError(f"Dataset folder not found: {SOURCE_DIR}")

# Process each class
for class_dir in sorted(SOURCE_DIR.iterdir()):

    if not class_dir.is_dir():
        continue

    class_name = class_dir.name

    # Find images
    images = [
        file for file in class_dir.iterdir()
        if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS
    ]

    # Shuffle images
    random.shuffle(images)

    total = len(images)

    train_end = int(total * TRAIN_RATIO)
    val_end = train_end + int(total * VAL_RATIO)

    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    print(f"\n{class_name}")
    print(f"  Total: {total}")
    print(f"  Train: {len(train_images)}")
    print(f"  Val:   {len(val_images)}")
    print(f"  Test:  {len(test_images)}")

    # Create destination folders
    for split in ["train", "val", "test"]:
        destination = OUTPUT_DIR / split / class_name
        destination.mkdir(parents=True, exist_ok=True)

    # Copy images
    for image in train_images:
        shutil.copy2(
            image,
            OUTPUT_DIR / "train" / class_name / image.name
        )

    for image in val_images:
        shutil.copy2(
            image,
            OUTPUT_DIR / "val" / class_name / image.name
        )

    for image in test_images:
        shutil.copy2(
            image,
            OUTPUT_DIR / "test" / class_name / image.name
        )

print("\n--------------------------------")
print("Dataset split completed!")
print(f"Output: {OUTPUT_DIR}")
print("--------------------------------")