def isMonotonic(array):
    if len(array) == 0 or len(array) == 1:
        return True
    # Assumption: Order is non-decreasing
    order = "INC"
    if array[0] > array[len(array) - 1]:
        order = "DEC"
    for index in range(len(array) - 1):
        if order == "INC":
            if array[index] > array[index + 1]:
                return False
        else:
            if array[index] < array[index + 1]:
                return False
    return True


class MonotonicArray:
    array = list(map(int, input().split()))
    print(isMonotonic(array))
