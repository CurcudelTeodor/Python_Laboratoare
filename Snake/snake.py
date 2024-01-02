from settings import *


class Snake:
    def __init__(self, canvas):
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
        # update the snake's position logic
        new_head = self.calculate_new_head()
        self.coordinates.insert(0, new_head)

        # remove the last body part
        self.coordinates = self.coordinates[:self.body_size]

    def grow(self):
        # increase the length of the snake by adding a new body part at the end
        tail_x, tail_y = self.coordinates[-1]
        self.coordinates.append((tail_x, tail_y))
        self.body_size += 1

    def calculate_new_head(self):
        # calculate the new head position based on the current direction
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
        self.canvas.delete("snake")

        for x, y in self.coordinates:
            square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

    def change_direction(self, new_direction):
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
        # check if the snake's head collides with the food
        head_x, head_y = self.coordinates[0]
        food_x, food_y = food_position
        return head_x == food_x and head_y == food_y

    def delete(self):
        for square in self.squares:
            self.canvas.delete(square)