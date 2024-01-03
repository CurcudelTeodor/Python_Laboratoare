"""
Snake Class

This module defines the Snake class, representing the snake entity in the game.

Attributes:
    canvas (tk.Canvas): The Tkinter canvas where the snake is drawn.
    body_size (int): The initial size of the snake's body.
    coordinates (list): List of (x, y) coordinates representing the snake's body parts.
    squares (list): List of Tkinter canvas rectangle objects representing snake body parts.
    direction (str): The current direction of the snake (e.g., "up", "down", "left", "right").

Methods:
    __init__(self, canvas)
        Initializes a new Snake object with the specified canvas.

    move(self)
        Updates the snake's position based on the current direction.

    calculate_new_head(self)
        Calculates the new head position based on the current direction.

    draw(self)
        Draws the snake on the canvas using rectangles.

    change_direction(self, new_direction)
        Changes the snake's direction based on user input.

    check_collision(self, food_position)
        Checks if the snake's head collides with the specified food position.

    grow(self)
        Increases the length of the snake by adding a new body part at the end.

    delete(self)
        Deletes the snake's graphical representation from the canvas.

"""
from settings import *


class Snake:
    def __init__(self, canvas):
        """
        Initializes a new Snake object.

        Parameters:
            canvas (tk.Canvas): The Tkinter canvas where the snake is drawn.
        """
        self.canvas = canvas
        self.body_size = BODY_PARTS
        self.coordinates = [(0, 0)]
        self.squares = []
        self.direction = "right"  # initial direction

        for _ in range(BODY_PARTS - 1):
            self.coordinates.append((0, 0))  # add initial body parts at (0, 0)

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

    def move(self):
        """
        Updates the snake's position based on the current direction.
        """
        # update the snake's position logic
        new_head = self.calculate_new_head()
        self.coordinates.insert(0, new_head)

        # remove the last body part
        self.coordinates = self.coordinates[:self.body_size]

    def calculate_new_head(self):
        """
        Calculates the new head position based on the current direction.

        Returns:
            tuple: The new head coordinates (x, y).
        """
        head_x, head_y = self.coordinates[0]

        if self.direction == "up":
            head_y -= SPACE_SIZE
        elif self.direction == "down":
            head_y += SPACE_SIZE
        elif self.direction == "left":
            head_x -= SPACE_SIZE
        elif self.direction == "right":
            head_x += SPACE_SIZE

        return head_x, head_y

    def draw(self):
        """
        Draws the snake on the canvas using rectangles.
        """
        self.canvas.delete("snake")

        for x, y in self.coordinates:
            square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

    def change_direction(self, new_direction):
        """
        Changes the snake's direction based on user input.

        Parameters:
            new_direction (str): The new direction ("up", "down", "left", "right").
        """
        valid_directions = ["up", "down", "left", "right"]
        current_direction = self.direction

        # check if the new direction is opposite to the current direction
        if (
            (current_direction == "up" and new_direction == "down") or
            (current_direction == "down" and new_direction == "up") or
            (current_direction == "left" and new_direction == "right") or
            (current_direction == "right" and new_direction == "left")
        ):
            return

        if new_direction in valid_directions:
            self.direction = new_direction

    def check_collision(self, food_position):
        """
        Checks if the snake's head collides with the specified food position.

        Parameters:
            food_position (tuple): The coordinates of the food (x, y).

        Returns:
            bool: True if collision occurs, False otherwise.
        """
        head_x, head_y = self.coordinates[0]
        food_x, food_y = food_position
        return head_x == food_x and head_y == food_y

    def grow(self):
        """
        Increases the length of the snake by adding a new body part at the end.
        """
        tail_x, tail_y = self.coordinates[-1]
        self.coordinates.append((tail_x, tail_y))
        self.body_size += 1

    def delete(self):
        """
        Deletes the snake's graphical representation from the canvas.
        """
        for square in self.squares:
            self.canvas.delete(square)
