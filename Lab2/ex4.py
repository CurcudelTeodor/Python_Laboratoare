def compose(notes, moves, start_position):
    song = []
    current_position = start_position
    song.append(notes[current_position])

    for move in moves:
        # Calculate the new position after the move, considering circular indexing
        current_position = (current_position + move) % len(notes)
        song.append(notes[current_position])

    return song


def main():
    notes = ["do", "re", "mi", "fa", "sol"]
    moves = [1, -3, 4, 2]
    start_position = 2
    result = compose(notes, moves, start_position)
    print(result)


if __name__ == "__main__":
    main()