import collections
from typing import List


class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        islands = 0

        for row in range(self.rows):
            for col in range(self.cols):
                islands += self.traverse(row, col, grid, visited)
        return islands

    def traverse(self, row, col, grid, visited):
        number_of_islands = 0
        queue = collections.deque()
        queue.append((row, col))
        while queue:
            x, y = queue.popleft()
            if visited[x][y] or grid[x][y] == "0":
                continue
            visited[x][y] = True
            number_of_islands += 1
            for neighbour in self.get_unvisited_neighbours(x, y, grid, visited):
                queue.append((neighbour[0], neighbour[1]))
        return 1 if number_of_islands > 0 else 0

    def get_unvisited_neighbours(self, row, col, grid, visited):
        neighbours = []
        if row > 0:
            neighbours.append((row - 1, col))
        if row < self.rows - 1:
            neighbours.append([row + 1, col])
        if col > 0:
            neighbours.append((row, col - 1))
        if col < self.cols - 1:
            neighbours.append([row, col + 1])
        return list(filter(lambda x: not visited[x[0]][x[1]] and grid[x[0]][x[1]] == "1", neighbours))


class NumberOfIslands:
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    x = Solution().numIslands(grid)
    print(x)
