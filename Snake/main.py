"""
main Module

This module contains the main entry point for the Snake game.

Functions:
    main()
        The main entry point for the Snake game.

"""
import sys
import traceback
from gui import create_game_window
from game import Game
import json

from settings import load_settings


def main():
    """
    The main entry point for the Snake game.

    This function reads the settings file path from the command line arguments,
    loads the game settings, creates the game window, and starts the game.

    Command Line Usage:
        python main.py <settings_file>

    Raises:
        SystemExit: If the command line arguments are invalid or an error occurs during execution.
    """
    if len(sys.argv) != 2:
        print("Usage: python main.py <settings_file>")
        sys.exit(1)

    settings_file = sys.argv[1]

    try:
        settings = load_settings(settings_file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: {e}")
        print(f"Error details: {e.doc}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        traceback.print_exc()
        sys.exit(1)

    window, canvas, label = create_game_window(settings)
    game = Game(canvas, settings, label)
    game.start()

    # start the Tkinter event loop and keep the GUI running, ensuring that the application remains interactive
    window.mainloop()


if __name__ == "__main__":
    main()
