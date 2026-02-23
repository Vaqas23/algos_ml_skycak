class Matrix:

    def __init__(self, arr):
        self.matrix = arr

        for i in range(len(arr)):
            if len(arr[0]) != len(arr[i]):
                raise TypeError(
                    "Each row must have an equal number of columns")

        self.num_row = len(arr)
        self.num_col = len(arr[0])

    def show(self):
        for row in self.matrix:
            print(f"{row}")

    def transpose(self):
        place_holder_matrix = []

        for i in range(self.num_col):
            place_holder_row = []
            for j in range(self.num_row):
                place_holder_row.append(self.matrix[j][i])
            place_holder_matrix.append(place_holder_row)

        self.matrix = place_holder_matrix
        self.num_row, self.num_col = self.num_col, self.num_row
        return self

    def add(self, other_arr):

        if self.num_row != other_arr.num_row or self.num_col != other_arr.num_col:
            raise TypeError(
                "You cannot add/subtract matrices of differing dimensions.")

        for i in range(self.num_row):
            for j in range(self.num_col):
                self.matrix[i][j] += other_arr.matrix[i][j]
        return self

    def subtract(self, other_arr):

        self.add(other_arr.scalar_multiply(-1))
        return self

    def scalar_multiply(self, scalar):

        for i in range(self.num_row):
            for j in range(self.num_col):
                self.matrix[i][j] *= scalar
        return self

    def matrix_multiply(self, other_arr):
        if self.num_col != other_arr.num_row:
            raise TypeError(
                "The number of columns in the first matrix must equal the number of rows in the second!")
        else:
            other_arr.transpose()
            resultant_matrix = []
            for i in range(self.num_row):
                row_matrix = []
                for j in range(other_arr.num_col):
                    row_matrix.append(dot_product(
                        self.matrix[i], other_arr.matrix[j]))
                resultant_matrix.append(row_matrix)

            other_arr.transpose()

            self.matrix = resultant_matrix
            return self

    def recursive_determinant(self):
        if self.num_col != self.num_row:
            raise TypeError(
                "Rows and Columns must be equal to take the determinant")
        else:
            return calculate_determinant(self.matrix)


def dot_product(arr1, arr2):
    if len(arr1) != len(arr2):
        raise TypeError("Vectors must be of equal length/dimension")
    else:
        dot_product_num = 0
        for i in range(len(arr1)):
            dot_product_num += arr1[i]*arr2[i]
        return dot_product_num


# Helper function for calculate_determinant
def remove_row_and_column(matrix, row, column):
    new_matrix = []
    for r in matrix:
        new_matrix.append(r[:]) # must copy in new matrix or else it would just be a reference and pop() the original Matrix object
    new_matrix.pop(row)
    for row in new_matrix:
        row.pop(column)
    return new_matrix

# Helper function for recursive_determinant that reduces overhead
# Ensure we dont need to make many Matrix objects
def calculate_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    determinant = 0
    for i in range(len(matrix[0])):
        sub_matrix = remove_row_and_column(matrix, 0, i)
        determinant += (-1)**i * matrix[0][i] * \
            calculate_determinant(sub_matrix)
    return determinant