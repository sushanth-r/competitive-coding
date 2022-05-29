def bubbleSort(array: list):
    is_array_sorted = False
    count = 0
    while not is_array_sorted:
        is_array_sorted = True
        for index in (range(len(array) - 1 - count)):
            if array[index] > array[index + 1]:
                swap(index, index + 1, array)
                is_array_sorted = False
        count += 1
    return array


def swap(i: int, j: int, array: list):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


class BubbleSort:
    array = list(map(int, input().split()))
    print(bubbleSort(array))
