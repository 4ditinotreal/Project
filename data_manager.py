import json, os

FILE = "students.json"

def load_data():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f)
