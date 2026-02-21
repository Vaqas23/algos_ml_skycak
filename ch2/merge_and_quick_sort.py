def merge(arr1, arr2):
    sorted_arr = []
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] > arr2[0]:
            sorted_arr.append(arr2[0])
            arr2.remove(arr2[0])
        else:
            sorted_arr.append(arr1[0])
            arr1.remove(arr1[0])
    if len(arr1) == 0:
        for num in arr2:
            sorted_arr.append(num)
    else:
        for num in arr1:
            sorted_arr.append(num)
    return sorted_arr


def merge_sort(arr):
    pass


def quick_sort(arr):
    pass
