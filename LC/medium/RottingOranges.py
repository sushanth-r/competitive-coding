import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh_count, rotten = 0, collections.deque()
        result = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_count += 1
                if grid[row][col] == 2:
                    rotten.append((row, col))

        while fresh_count > 0 and rotten:
            length = len(rotten)

            for i in range(length):
                x, y = rotten.popleft()
                for direction in directions:
                    i, j = x + direction[0], y + direction[1]
                    if 0 <= i <= rows - 1 and 0 <= j <= cols - 1 and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh_count -= 1
                        rotten.append((i, j))
            result += 1

        return result if fresh_count == 0 else -1


class RottingOranges:
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    x = Solution().orangesRotting(grid)
    print(x)
