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
    pass


def quick_sort(arr):
    pass
