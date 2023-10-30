def find_obstructed_seats(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    obstructed_seats = []

    for i in range(rows - 1, -1, -1):  # Start from the last row and move upwards (I'm going in reverse order)
        for j in range(cols):
            current_height = matrix[i][j]
            obstructed = False

            # Check if there is a taller spectator in front (above) of the current cell
            for k in range(i - 1, -1, -1):
                if matrix[k][j] >= current_height:
                    obstructed = True
                    break

            if obstructed:
                obstructed_seats.append((i, j))

    return obstructed_seats


def main():
    stadium_heights = [
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
    ]

    obstructed_seats = find_obstructed_seats(stadium_heights)
    print(obstructed_seats)


if __name__ == "__main__":
    main()
