def sortedSquaredArray(array):
    return sorted(list(map(lambda x: x**2, array)))


class SortedSquaredArray:
    array = list(map(int, input().split()))
    print(sortedSquaredArray(array))
