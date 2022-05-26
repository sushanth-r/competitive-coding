import collections
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])
        queue = collections.deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    queue.append((row, col))

        while queue:
            x, y = queue.popleft()
            for i, j in directions:
                if x + i < 0 or x + i > rows - 1 or y + j < 0 \
                        or y + j > cols - 1 or rooms[x + i][y + j] <= rooms[x][y]:
                    continue
                rooms[x + i][y + j] = 1 + rooms[x][y]
                queue.append((x + i, y + j))


class WallsAndGates:
    rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]
    Solution().wallsAndGates(rooms)
    print(rooms)
