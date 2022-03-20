# O(n) - Time & O(1) - Space
def firstDuplicateValue(array):
    for index in range(len(array)):
        value = array[index]
        mod = abs(value)
        if array[mod - 1] < 0:
            return mod
        array[mod - 1] = -array[mod - 1]
    return -1


class FirstDuplicateValue:
    array = list(map(int, input().split()))
    print(firstDuplicateValue(array))
