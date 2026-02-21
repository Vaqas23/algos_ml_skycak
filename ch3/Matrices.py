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
        pass

    def add(self, other_arr):

        if self.num_row != other_arr.num_row or self.num_col != other_arr.num_col:
            raise TypeError(
                "You cannot add/subtract matrices of differing dimensions.")

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] += other_arr.matrix[i][j]
        return self

    def subtract(self, other_arr):

        self.add(other_arr.scalar_multiply(-1))
        return self

    def scalar_multiply(self, scalar):

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] *= scalar
        return self


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
matrix1.subtract(matrix2).show()
