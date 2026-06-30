from flask import Flask, render_template, request
import os

from predict import predict_image
from utils import get_disease_info
from utils import format_class_name
app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    filename = file.filename

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    class_name, confidence = predict_image(filepath)

    info = get_disease_info(class_name)

    if info is None:

        info = {

            "plant": class_name.split("___")[0].replace("_", " "),

            "disease": class_name.split("___")[1].replace("_", " "),

            "latin_name": "-",

            "severity": "Noma'lum",

            "description": "Ma'lumot topilmadi.",

            "symptoms": "Ma'lumot topilmadi.",

            "causes": "Ma'lumot topilmadi.",

            "treatment": "Ma'lumot topilmadi.",

            "prevention": "Ma'lumot topilmadi."

        }

    return render_template(

        "result.html",

        image="/" + filepath.replace("\\", "/"),

        confidence=round(confidence, 2),

        plant=info["plant"],

        disease=info["disease"],

        latin_name=info["latin_name"],

        severity=info["severity"],

        description=info["description"],

        symptoms=info["symptoms"],

        causes=info["causes"],

        treatment=info["treatment"],

        prevention=info["prevention"]

    )


if __name__ == "__main__":
    app.run(debug=True)