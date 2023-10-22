def spiral_order_matrix(matrix):
    result = []
    while matrix:
        #  + -> concatenate lists (can't do list + string)
        #  append -> concatenate list with a string
        #  left -> right: remove the 1st row (with index 0)
        result = result + matrix.pop(0)

        #  top -> bottom: check if matrix is not empty and if I have 1st row (2nd row after I popped the 1st earlier)
        #  optional condition for matrix because if there is a row (matrix[0]), then the matrix is non-empty. Tho,
        #  matrix might be an empty list or a list with empty sublists, so it's better to keep it there (edge cases ->
        #  robustness)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        #  right -> left: If we got here, there is sure at least one row -> We don't have to check for matrix[0]
        #  We pop the last row (matrix.pop()) and reverse the order: [::-1]
        if matrix:
            result = result + matrix.pop()[::-1]

        #  bottom -> top: We need the matrix[0] check because row.pop(0) will be performed, which means it will remove
        #  the first element of the first row.
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))

    return ''.join(result)


def main():
    matrix = [
        ['f', 'i', 'r', 's'],
        ['n', '_', 'l', 't'],
        ['o', 'b', 'a', '_'],
        ['h', 't', 'y', 'p']
    ]

    result = spiral_order_matrix(matrix)

    print("Resulting string: %s" % result)


if __name__ == "__main__":
    main()

#   matrix.pop(0)
#     print(matrix)
#
#     result = []
#     for row in matrix:
#         print(result + row.pop())
#
#     print(matrix)
#     print(matrix.pop()[::-1])
#     print(matrix[::-1])
#     return 0
