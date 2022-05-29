def selectionSort(array: list):
    i = 0
    while i < len(array) - 1:
        smallest_index = i
        j = i + 1
        while j < len(array):
            if array[j] < array[smallest_index]:
                smallest_index = j
            j += 1
        swap(i, smallest_index, array)
        i += 1
    return array


def swap(i: int, j: int, array: list):
    array[i], array[j] = array[j], array[i]


class SelectionSort:
    array = list(map(int, input().split()))
    print(selectionSort(array))
