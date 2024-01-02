import sys
import traceback
import gui
import json

from settings import load_settings


def main():
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
        traceback.print_exc()  # Print the full traceback for debugging
        sys.exit(1)

    # main entry point
    # game.start_game(settings_file)
    gui.create_game_window(settings)


if __name__ == "__main__":
    main()