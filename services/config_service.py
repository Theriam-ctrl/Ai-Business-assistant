import json


def load_config():

    with open("data/business_config.json", "r") as file:
        return json.load(file)