import random


def merge(arr1, arr2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            sorted_arr.append(arr2[j])
            j += 1
        else:
            sorted_arr.append(arr1[i])
            i += 1
    sorted_arr.extend(arr1[i:])
    sorted_arr.extend(arr2[j:])
    return sorted_arr


def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        first_half = arr[0: len(arr)//2]
        second_half = arr[len(arr)//2:]
        merged_first_half = merge_sort(first_half)
        merged_second_half = merge_sort(second_half)
        return merge(merged_first_half, merged_second_half)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less_than_pivot = []
        more_than_pivot = []
        pivots = []
        for num in arr:
            if num < pivot:
                less_than_pivot.append(num)
            elif num > pivot:
                more_than_pivot.append(num)
            else:
                pivots.append(num)
        less_sorted = quick_sort(less_than_pivot)
        more_sorted = quick_sort(more_than_pivot)
        return less_sorted + pivots + more_sorted


print(quick_sort([1, 8, -9, 2, 3, 7, 8, 110, -200, 6, 2, 5]))
