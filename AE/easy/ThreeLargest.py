import sys


def findThreeLargestNumbers(array):
    third_largest = - sys.maxsize
    second_largest = third_largest + 1
    largest = second_largest + 1
    for element in array:
        if element >= largest:
            third_largest = second_largest
            second_largest = largest
            largest = element
        elif element >= second_largest:
            third_largest = second_largest
            second_largest = element
        elif element >= third_largest:
            third_largest = element
    return [third_largest, second_largest, largest]


class ThreeLargest:
    # array = list(map(int, input().split()))
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    print(findThreeLargestNumbers(array))
