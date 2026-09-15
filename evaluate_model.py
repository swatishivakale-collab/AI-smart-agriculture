import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from pathlib import Path
from sklearn.metrics import confusion_matrix, classification_report

# =========================
# CONFIGURATION
# =========================

TEST_DIR = Path("dataset_split/test")
MODEL_PATH = Path("ai_model/tomato_disease_model_v2.keras")

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32


# =========================
# LOAD MODEL
# =========================

print("Loading trained model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Model loaded successfully!")


# =========================
# LOAD TEST DATASET
# =========================

print("\nLoading test dataset...")

test_ds = tf.keras.utils.image_dataset_from_directory(
    TEST_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="categorical",
    shuffle=False,
)

class_names = test_ds.class_names

print("\nClasses:")
for i, name in enumerate(class_names):
    print(f"{i}: {name}")


# =========================
# GET TRUE LABELS
# =========================

print("\nRunning predictions...")

y_true = []
y_pred = []

for images, labels in test_ds:

    predictions = model.predict(images, verbose=0)

    predicted_classes = np.argmax(predictions, axis=1)
    true_classes = np.argmax(labels.numpy(), axis=1)

    y_pred.extend(predicted_classes)
    y_true.extend(true_classes)


y_true = np.array(y_true)
y_pred = np.array(y_pred)


# =========================
# CONFUSION MATRIX
# =========================

cm = confusion_matrix(y_true, y_pred)

print("\n==============================")
print("CONFUSION MATRIX")
print("==============================")

print(cm)
# =========================
# PLOT CONFUSION MATRIX
# =========================

plt.figure(figsize=(9, 7))

plt.imshow(cm)

plt.title("Tomato Disease Confusion Matrix")
plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")

plt.xticks(
    range(len(class_names)),
    class_names,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(class_names)),
    class_names
)

# Display numbers inside the matrix
for i in range(len(class_names)):
    for j in range(len(class_names)):
        plt.text(
            j,
            i,
            cm[i, j],
            ha="center",
            va="center"
        )

plt.tight_layout()

# Save image
plt.savefig("confusion_matrix.png")

print("\nConfusion matrix saved to: confusion_matrix.png")

plt.show()

# =========================
# CLASSIFICATION REPORT
# =========================

print("\n==============================")
print("CLASSIFICATION REPORT")
print("==============================")

print(
    classification_report(
        y_true,
        y_pred,
        target_names=class_names,
        digits=4
    )
)


# =========================
# TEST ACCURACY
# =========================

accuracy = np.mean(y_true == y_pred)

print("==============================")
print(f"TEST ACCURACY: {accuracy:.4f}")
print("==============================")

print("\nEvaluation completed successfully!")