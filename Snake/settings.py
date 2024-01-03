"""
settings Module

This module provides constants and functions for managing game settings.

Constants:
    INITIAL_SPEED (int): The initial speed of the game.
    SPEED_INCREASE_FACTOR (int): The factor by which the speed increases.
    SPACE_SIZE (int): The size of each cell in the game grid.
    BODY_PARTS (int): The initial number of body parts for the snake.
    SNAKE_COLOR (str): The color of the snake.
    FOOD_COLOR (str): The color of the food.
    BACKGROUND_COLOR (str): The background color of the game.

Functions:
    load_settings(file_path)
        Loads game settings from a JSON file.

"""
import json

INITIAL_SPEED = 100
SPEED_INCREASE_FACTOR = 3
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


def load_settings(file_path):
    """
    Loads game settings from a JSON file.

    Parameters:
        file_path (str): The path to the JSON file containing game settings.

    Returns:
        dict: Dictionary containing the loaded game settings.

    Raises:
        FileNotFoundError: If the specified file is not found.
        json.JSONDecodeError: If there is an issue parsing JSON in the file.
        Exception: If an unexpected error occurs while loading settings.
    """
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
