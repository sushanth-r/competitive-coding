import collections
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1 or board[i][j] != "O":
                return
            if board[i][j] == "O":
                board[i][j] = "$"

            for direction in directions:
                dfs(i + direction[0], j + direction[1])

        for row in range(rows):
            for col in range(cols):
                if (row == 0 or row == rows - 1 or col == 0 or col == cols - 1) and board[row][col] == "O":
                    dfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "$":
                    board[row][col] = "O"


class SurroundedRegions:
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Solution().solve(board)
    print(board)
