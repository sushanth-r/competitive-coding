from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        if matrix[rows - 1][cols - 1] < target:
            return False
        i = j = 0
        while i < rows - 1 and matrix[i + 1][j] <= target:
            i += 1
        while j < cols and matrix[i][j] < target:
            j += 1
        return i < rows and j < cols and matrix[i][j] == target


class Search2DMatrix:
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = int(input())
    solution = Solution()
    x = solution.searchMatrix(matrix, target)
    print(x)
