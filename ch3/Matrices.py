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

    def add(self):
        pass

    def subtract(self):
        pass

    def scalar_multiply(self):
        pass


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix.show()
