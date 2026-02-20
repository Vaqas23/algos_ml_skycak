# calculate and return the minimum value in an array, cant use min() function
def calc_min(arr):
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        min_value = calc_min(arr)
        sorted_arr.append(min_value)
        arr.remove(min_value)
    return sorted_arr
