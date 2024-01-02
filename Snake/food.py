import random
from settings import *


class Food:
    def __init__(self, canvas, settings, snake, obstacles):
        self.canvas = canvas
        self.settings = settings
        self.snake = snake
        self.position = (0, 0)  # initial position of the food
        self.obstacles = obstacles
        self.spawn_food()

    def spawn_food(self):
        # randomly place the food on the canvas within the game boundaries
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
        self.canvas.create_oval(
            self.position[0], self.position[1],
            self.position[0] + SPACE_SIZE, self.position[1] + SPACE_SIZE,
            fill="#FF0000", tag="food"
        )

    def delete(self):
        self.canvas.delete("food")
