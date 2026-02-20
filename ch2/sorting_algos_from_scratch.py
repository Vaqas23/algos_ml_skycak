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


def bubble_sort(arr):
    while True:  # if swap happens, swap = True, else swap = False, break
        swap = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                smaller = arr[i]
                bigger = arr[i-1]
                arr[i-1] = smaller
                arr[i] = bigger
                swap = True
        if swap == False:
            break
    return arr
