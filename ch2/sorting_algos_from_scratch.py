# calculate and return the minimum value in an array, cant use min() function
def calc_min(arr):
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min


def calc_max(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        min_value = calc_min(arr)
        sorted_arr.append(min_value)
        arr.remove(min_value)
    return sorted_arr


def bubble_sort(arr):
    while True:
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


def insertion_sort(arr):
    for i in range(1, len(arr)):
        while i > 0:
            if arr[i] < arr[i-1]:
                smaller = arr[i]
                bigger = arr[i-1]
                arr[i-1] = smaller
                arr[i] = bigger
                i -= 1
            else:
                break
    return arr


def counting_sort(arr):

    # step 1
    smallest = calc_min(arr)
    for i in range(len(arr)):
        arr[i] = arr[i] - smallest

    # step 2
    largest = calc_max(arr)
    counts = [0] * (largest + 1)

    # step 3
    for num in arr:
        counts[num] += 1

    # step 4
    sorted_arr = []
    for i in range(len(counts)):
        num = counts[i]
        for j in range(num):
            sorted_arr.append(i)

    # step 5
    for i in range(len(sorted_arr)):
        sorted_arr[i] = sorted_arr[i] + smallest

    return sorted_arr


# Example of when counting sort would be impractical. Array contains a count of every number
# from smallest to largest (-10000 to 1000 in this case)
# print(counting_sort([1, 2, 4, 3, 6, 5, 0, 1000, -10000, 30]))
