from tkinter import Tk, Canvas, Label
from settings import *


def create_game_window(settings):
    board_width = settings.get("board_width", 10)
    board_height = settings.get("board_height", 10)

    window = Tk()
    window.title("Snake game")
    window.resizable(False, False)

    # adding a score label
    score = 0
    label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
    label.pack()

    # creating a canvas for the snake
    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=board_height * SPACE_SIZE, width=board_width * SPACE_SIZE)
    canvas.pack()

    center_window(window)

    return window, canvas, label


def center_window(window):
    # make sure that the information (width and height) I get is up-to-date (processed internal tasks)
    # done to ensure that the window has processed any pending idle tasks and has updated its dimensions before
    # attempting to use them in calculations
    window.update_idletasks()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
