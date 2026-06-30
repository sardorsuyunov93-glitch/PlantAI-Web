import json


def load_disease_database():

    with open(
        "disease_info.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def get_disease_info(class_name):

    database = load_disease_database()

    return database.get(class_name, None)


def format_class_name(class_name):

    parts = class_name.split("___")

    plant = parts[0].replace("_", " ")

    disease = parts[1].replace("_", " ")

    return plant, disease