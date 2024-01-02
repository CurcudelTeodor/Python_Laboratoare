from tkinter import Tk, Canvas, Label

SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


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

    window.mainloop()


def center_window(window):
    window.update_idletasks()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")


