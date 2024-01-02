import json


def load_settings(file_path):
    try:
        with open(file_path, "r") as file:
            settings = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error: Unable to parse JSON in file '{file_path}': {e}", e.doc, e.pos)

    return settings
