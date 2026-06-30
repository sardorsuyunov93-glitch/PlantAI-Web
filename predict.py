import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input

# Modelni yuklash
interpreter = tf.lite.Interpreter(
    model_path="model/plant_disease_model.tflite"
)

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Labels
with open("labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]


def predict_image(image_path):

    image = Image.open(image_path).convert("RGB")

    image = image.resize((224, 224))

    image = np.array(image, dtype=np.float32)

    image = preprocess_input(image)

    image = np.expand_dims(image, axis=0)

    interpreter.set_tensor(
        input_details[0]["index"],
        image
    )

    interpreter.invoke()

    prediction = interpreter.get_tensor(
        output_details[0]["index"]
    )[0]

    index = np.argmax(prediction)

    confidence = float(prediction[index]) * 100

    disease = labels[index]

    print("\n" + "=" * 60)
    print("MODEL RETURNED :", disease)
    print("CONFIDENCE     :", round(confidence, 2), "%")
    print("=" * 60)

    # TOP 5 natijalar
    top5 = np.argsort(prediction)[-5:][::-1]

    print("TOP 5 PREDICTIONS")

    for i in top5:
        print(
            f"{i:2d} | {labels[i]:40} | {prediction[i] * 100:.2f}%"
        )

    print("=" * 60)

    return disease, confidence