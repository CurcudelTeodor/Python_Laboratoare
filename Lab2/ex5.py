def zero_below_main_diagonal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Iterate and replace elements under the main diagonal with 0
    for i in range(rows):
        for j in range(cols):
            if j < i:
                matrix[i][j] = 0
    return matrix


def main():

    matrix = [
        [4, 5, 7],
        [43, 2, 86],
        [1, 99, 2]
    ]

    result_matrix = zero_below_main_diagonal(matrix)
    for row in result_matrix:
        print(row)


if __name__ == "__main__":
    main()