def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1
    return array


def swap(i: int, j: int, array: list):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


class InsertionSort:
    array = list(map(int, input().split()))
    print(insertionSort(array))
