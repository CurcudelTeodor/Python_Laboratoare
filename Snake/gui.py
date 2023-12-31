import json
import sys
from tkinter import Tk, Canvas
from settings import load_settings

SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


def create_game_window():
    try:
        settings_file = sys.argv[1]
    except IndexError:
        print("Usage: python gui.py <settings_file>")
        sys.exit(1)

    try:
        settings = load_settings(settings_file)
    except FileNotFoundError:
        print(f"Error: File '{settings_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Unable to parse JSON in file '{settings_file}'.")
        sys.exit(1)

    board_width = settings.get("board_width", 10)
    board_height = settings.get("board_height", 10)

    window = Tk()
    window.title("Snake game")
    window.resizable(False, False)

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=board_height * SPACE_SIZE, width=board_width * SPACE_SIZE)
    canvas.pack()

    window.mainloop()


if __name__ == "__main__":
    create_game_window()
