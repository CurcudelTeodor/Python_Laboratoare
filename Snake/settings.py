import json

INITIAL_SPEED = 100
SPEED_INCREASE_FACTOR = 3
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


def load_settings(file_path):
    try:
        with open(file_path, "r") as file:
            settings = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error: Unable to parse JSON in file '{file_path}': {e}", e.doc, e.pos)
    except Exception as e:
        raise Exception(f"An unexpected error occurred while loading settings from '{file_path}': {e}")

    return settings
