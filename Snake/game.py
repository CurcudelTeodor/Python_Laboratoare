import os
import tkinter as tk
from snake import Snake
from food import Food
from settings import *


class Game:
    def __init__(self, canvas, settings, label):
        self.canvas = canvas
        self.settings = settings
        self.label = label

        self.snake = Snake(self.canvas)
        self.current_speed = INITIAL_SPEED

        # load and draw obstacles
        self.obstacles = settings.get("obstacles", [])
        self.draw_obstacles()

        self.food = Food(self.canvas, self.settings, self.snake, self.obstacles)

        self.score = 0
        self.high_score = self.load_high_score()

        self.game_over_message = None
        self.play_again_button = None
        self.exit_button = None
        self.high_score_label = None

    def start(self):
        self.canvas.bind_all('<Key>', self.on_key_press)
        # starting the main game loop
        self.next_turn()

    def on_key_press(self, event):
        # print(event.keysym)
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.snake.change_direction(event.keysym.lower())  # convert to lowercase for consistency

    def next_turn(self):
        # update game logic here (move snake, check collisions, ...)
        self.snake.move()
        self.check_collisions()

        self.food.draw()
        self.snake.draw()

        # check for game over condition
        if self.game_over_message is None:
            self.canvas.after(self.current_speed, self.next_turn)

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            x, y = obstacle["x"] * SPACE_SIZE, obstacle["y"] * SPACE_SIZE
            self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill='gray', tag="obstacle")

    def load_high_score(self):
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as file:
                try:
                    return int(file.read())
                except ValueError:
                    print("Error: The file does not contain a valid integer for high score.")
        return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def show_high_score(self):
        # additional precaution for unexpected scenarios where destroy() is called without a valid label
        if self.high_score_label:
            self.high_score_label.destroy()

        x = self.canvas.winfo_reqwidth() // 2
        y = self.canvas.winfo_reqheight() // 2 - 100
        self.high_score_label = tk.Label(
            self.canvas,
            text=f"High Score: {self.high_score}",
            font=('consolas', 20),
            fg='yellow',
            bg=BACKGROUND_COLOR
        )
        self.high_score_label.place(x=x, y=y, anchor=tk.CENTER)
        self.canvas.after(3000, self.clear_high_score_label)

    def clear_high_score_label(self):
        if self.high_score_label:
            self.high_score_label.destroy()

    def check_collisions(self):
        # check collision with food
        if self.snake.check_collision(self.food.position):
            self.current_speed -= SPEED_INCREASE_FACTOR

            self.score += 1
            self.label.config(text=f"Score: {self.score}")
            print(self.score)

            self.food.delete()
            self.food.spawn_food()

            self.snake.grow()

        head_x, head_y = self.snake.coordinates[0]

        # check if the snake's head collides with the window borders
        board_width = self.settings["board_width"]
        board_height = self.settings["board_height"]
        if head_x < 0 or head_x >= board_width * 50 or head_y < 0 or head_y >= board_height * 50:
            self.game_over()
            return

        # check if the snake's head collides with its own body
        if (head_x, head_y) in self.snake.coordinates[1:]:
            self.game_over()
            return

        # check if the snake's head collides with obstacles
        if (head_x, head_y) in [(obstacle["x"] * SPACE_SIZE, obstacle["y"] * SPACE_SIZE) for obstacle in self.obstacles]:
            self.game_over()
            return

    def game_over(self):
        # check and update the high score
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

        # display "Game Over" message on the canvas
        if self.game_over_message is None:
            x = self.canvas.winfo_reqwidth() // 2
            y = self.canvas.winfo_reqheight() // 2

            self.game_over_message = tk.Label(
                self.canvas,
                text="GAME OVER",
                font=('consolas', 40),
                fg='red',
                bg=BACKGROUND_COLOR
            )
            self.game_over_message.place(x=x, y=y-30, anchor=tk.CENTER)

            self.play_again_button = tk.Button(
                self.canvas.master, text="Play Again", command=self.play_again
            )
            self.play_again_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

            self.exit_button = tk.Button(
                self.canvas.master, text="Exit", command=self.show_high_score_and_exit
            )
            self.exit_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def show_high_score_and_exit(self):
        self.show_high_score()
        self.canvas.master.after(3000, self.canvas.master.destroy)

    def play_again(self):
        # reset the game state and start a new game
        self.game_over_message.destroy()
        self.play_again_button.destroy()
        self.exit_button.destroy()

        self.game_over_message = None
        self.score = 0
        self.label.config(text=f"Score: {self.score}")
        self.canvas.delete("snake")
        self.canvas.delete("food")
        self.current_speed = INITIAL_SPEED
        # reset obstacles
        self.obstacles = self.settings.get("obstacles", [])
        self.draw_obstacles()

        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas, self.settings, self.snake, self.obstacles)
        self.play_again_button.destroy()
        self.exit_button.destroy()
        self.next_turn()
