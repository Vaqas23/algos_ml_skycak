# calculate and return the minimum value in an array, cant use min() function
def calc_min(arr):
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min
