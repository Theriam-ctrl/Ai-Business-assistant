import json
from datetime import datetime

def get_all_leads():

    with open("data/leads.json", "r") as file:
        return json.load(file)


def save_lead(name, phone):
    leads = get_all_leads()

    leads.append(
        {
            "name": name,
            "phone": phone,
            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }
    )

    with open("data/leads.json", "w") as file:
        json.dump(leads, file, indent=4)