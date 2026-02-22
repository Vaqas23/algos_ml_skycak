class Matrix:

    def __init__(self, arr):
        self.matrix = arr
        self.num_row = 0
        self.num_col = 0

        for i in range(len(arr)):
            if len(arr[0]) != len(arr[i]):
                raise TypeError(
                    "Each row must have an equal number of columns")

        for row in arr:
            self.num_row += 1
        for i in range(len(arr[0])):
            self.num_col += 1

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
        if len(self.matrix[0]) != len(other_arr):
            raise TypeError(
                "The number of columns in the first matrix must equal the number of rows in the second!")
        else:
            other_arr_transpoed = other_arr.transpose()
            for i in range(self.num_row):
                for i in range(len(other_arr.matrix.num_col)):


def dot_product(arr1, arr2):
    if len(arr1) != len(arr2):
        raise TypeError("Vectors must be of equal length/dimension")
    else:
        dot_product = 0
        for i in range(len(arr1)):
            dot_product += arr1[i]*arr2[i]
        return dot_product
