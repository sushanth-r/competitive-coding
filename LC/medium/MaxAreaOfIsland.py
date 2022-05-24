import collections
from typing import List


class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.grid = [[]]
        self.visited = [[]]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        visited = [[False for _ in range(self.cols)] for row in range(self.rows)]
        self.grid, self.visited = grid, visited

        max_area = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 0 or self.visited[row][col]:
                    continue
                max_area = max(max_area, self.bfs(row, col))
        return max_area

    def bfs(self, row, col):
        area = 0
        queue = collections.deque()
        queue.append((row, col))
        while queue:
            x, y = queue.popleft()
            if self.visited[x][y] or self.grid[x][y] == 0:
                continue
            self.visited[x][y] = True
            neighbours = self.get_unvisited_neighbours(x, y)
            area += 1
            for neighbour in neighbours:
                queue.append((neighbour[0], neighbour[1]))
        return area

    def get_unvisited_neighbours(self, row, col):
        neighbours = []
        if row > 0:
            neighbours.append((row - 1, col))
        if row < self.rows - 1:
            neighbours.append((row + 1, col))
        if col > 0:
            neighbours.append((row, col - 1))
        if col < self.cols - 1:
            neighbours.append((row, col + 1))
        return list(filter(lambda x: self.grid[x[0]][x[1]] == 1
                                     and (not self.visited[x[0]][x[1]]), neighbours))


class MaxAreaOfIsland:
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    x = Solution().maxAreaOfIsland(grid)
    print(x)
