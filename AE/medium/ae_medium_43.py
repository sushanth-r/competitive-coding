def searchInSortedMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    i = 0
    j = cols - 1
    while i < rows and j > -1:
        if matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
        else:
            return [i, j]
    return [-1, -1]


class SearchInSortedMatrix:
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ]
    target = int(input())
    print(searchInSortedMatrix(matrix, target))
