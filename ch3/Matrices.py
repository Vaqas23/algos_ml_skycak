class Matrix:

    def __init__(self, arr):
        self.num_row = 0
        self.num_col = 0

        for i in range(len(arr)):
            if arr[0] != arr[i]:
                raise TypeError(
                    "Each row must have an equal number of columns")

        for row in arr:
            self.num_row += 1
        for i in range(len(arr[0])):
            self.num_col += 1

    def show(self):
        pass

    def transpose(self):
        pass

    def add(self):
        pass

    def subtract(self):
        pass

    def scalar_multiply(self):
        pass
