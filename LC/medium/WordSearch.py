import collections
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or (r, c) in visited or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            visited.add((r, c))
            result = dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1) or dfs(r - 1, c, i + 1) \
                     or dfs(r + 1, c, i + 1)
            visited.remove((r, c))
            return result

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False


class WordSearch:
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = input()
    x = Solution().exist(board, word)
    print(x)
