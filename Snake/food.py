"""
Food Class

This module defines the Food class, representing the food entity in the game.

Attributes:
    canvas (tk.Canvas): The Tkinter canvas where the food is drawn.
    settings (dict): Dictionary containing game settings.
    snake (Snake): The Snake object representing the game's snake.
    position (tuple): The current position of the food (x, y).
    obstacles (list): List of obstacles on the game board.

Methods:
    __init__(self, canvas, settings, snake, obstacles)
        Initializes a new Food object with the specified canvas, settings, snake, and obstacles.

    spawn_food(self)
        Randomly places the food on the canvas within the game boundaries.

    draw(self)
        Draws the food on the canvas.

    delete(self)
        Deletes the food's graphical representation from the canvas.

"""

import random
from settings import *


class Food:
    def __init__(self, canvas, settings, snake, obstacles):
        """
        Initializes a new Food object.

        Parameters:
            canvas (tk.Canvas): The Tkinter canvas where the food is drawn.
            settings (dict): Dictionary containing game settings.
            snake (Snake): The Snake object representing the game's snake.
            obstacles (list): List of obstacles on the game board.
        """
        self.canvas = canvas
        self.settings = settings
        self.snake = snake
        self.position = (0, 0)  # initial position of the food
        self.obstacles = obstacles
        self.spawn_food()

    def spawn_food(self):
        """
        Randomly places the food on the canvas within the game boundaries.
        """
        board_width = self.settings["board_width"]
        board_height = self.settings["board_height"]

        # keep generating random coordinates until an empty spot is found
        while True:
            x = random.randint(0, (board_width - 1)) * SPACE_SIZE
            y = random.randint(0, (board_height - 1)) * SPACE_SIZE

            # check if the generated coordinates collide with the snake and the obstacles
            if (x, y) not in self.snake.coordinates and (x, y) not in [(obstacle["x"] * SPACE_SIZE, obstacle["y"] * SPACE_SIZE) for obstacle in self.obstacles]:
                break

        self.position = (x, y)

    def draw(self):
        """
        Draws the food on the canvas.
        """
        self.canvas.create_oval(
            self.position[0], self.position[1],
            self.position[0] + SPACE_SIZE, self.position[1] + SPACE_SIZE,
            fill="#FF0000", tag="food"
        )

    def delete(self):
        """
        Deletes the food's graphical representation from the canvas.
        """
        self.canvas.delete("food")
