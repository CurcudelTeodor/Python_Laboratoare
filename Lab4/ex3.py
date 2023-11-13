class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def get_element(self, i, j):
        return self.data[i][j]

    def set_element(self, i, j, value):
        self.data[i][j] = value

    def transpose(self):
        self.data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        self.rows, self.cols = self.cols, self.rows

    def matrix_multiply(self, other_matrix):
        if self.cols != other_matrix.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second "
                             "matrix.")

        result = Matrix(self.rows, other_matrix.cols)

        for i in range(self.rows):
            for j in range(other_matrix.cols):
                # Calculam produsul (dot product) dintre linia i a primei matrici si coloana j de la a doua matrice
                # si facem suma
                result.data[i][j] = sum(self.data[i][k] * other_matrix.data[k][j] for k in range(self.cols))

        return result

    def apply_transform(self, transform_func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = transform_func(self.data[i][j])

    def __str__(self):
        # String representation of the matrix for better visualization
        return "\n".join([" ".join(map(str, row)) for row in self.data])


def main():

    matrix_a = Matrix(2, 3)

    matrix_a.set_element(0, 0, 4)
    matrix_a.set_element(0, 1, 2)
    matrix_a.set_element(0, 2, 6)
    matrix_a.set_element(1, 0, 8)
    matrix_a.set_element(1, 1, 1)
    matrix_a.set_element(1, 2, 9)

    print("Matrix A:")
    print(matrix_a)

    matrix_b = Matrix(3, 2)
    matrix_b.set_element(0, 0, 4)
    matrix_b.set_element(0, 1, 1)
    matrix_b.set_element(1, 0, 6)
    matrix_b.set_element(1, 1, 7)
    matrix_b.set_element(2, 0, 9)
    matrix_b.set_element(2, 1, 5)

    print("\nMatrix B:")
    print(matrix_b)

    result = matrix_a.matrix_multiply(matrix_b)
    print("\nMatrix A * Matrix B:")
    print(result)

    result.transpose()
    print("\nTranspose of Matrix A * Matrix B:")
    print(result)

    # Example of applying a transformation (squaring each element)
    matrix_a.apply_transform(lambda x: x**3)
    print("\nMatrix A after applying a transformation (cube each element):")
    print(matrix_a)

    print("-\-\-\-\-\-\-\-\-\--\\-\-\-\-\-\-\-\\-\-")

    # Example without updating dimensions after transpose
    matrix_a = Matrix(3, 2)
    matrix_a.set_element(0, 0, 1)
    matrix_a.set_element(0, 1, 2)
    matrix_a.set_element(1, 0, 4)
    matrix_a.set_element(1, 1, 5)
    matrix_a.set_element(2, 0, 6)
    matrix_a.set_element(2, 1, 6)


    matrix_b = Matrix(3, 2)
    matrix_b.set_element(0, 0, 7)
    matrix_b.set_element(0, 1, 8)
    matrix_b.set_element(1, 0, 9)
    matrix_b.set_element(1, 1, 10)
    matrix_b.set_element(2, 0, 11)
    matrix_b.set_element(2, 1, 12)

    print("Matrix A:")
    print(matrix_a)

    print("\nMatrix B:")
    print(matrix_b)

    matrix_a.transpose()

    print("\nTransposed Matrix A:")
    print(matrix_a)

    print("\nTransposed Matrix A with Matrix B")
    # Try to multiply transposed Matrix A with Matrix B
    result = matrix_a.matrix_multiply(matrix_b)
    print(result)


if __name__ == "__main__":
    main()