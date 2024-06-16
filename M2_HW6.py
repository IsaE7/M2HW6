def bubble_sort(arr):

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr, val):

    first = 0
    last = len(arr) - 1
    result_ok = False
    pos = -1

    while first <= last and not result_ok:
        middle = (first + last) // 2
        if arr[middle] == val:
            result_ok = True
            pos = middle
        else:
            if val < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1

    if result_ok:
        print("Элемент найден на позиции:", pos)
    else:
        print("Элемент не найден")


arr = [64, 34, 25, 12, 22, 11, 90]

sorted_arr = bubble_sort(arr)
print("Отсортированный список:", sorted_arr)

val = 25
binary_search(sorted_arr, val)
