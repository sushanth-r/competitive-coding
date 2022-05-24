from typing import List


class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.heights = [[]]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, visit, prev_height):
            if (r, c) in visit or r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or heights[r][c] < prev_height:
                return
            visit.add((r, c))
            for direction in directions:
                dfs(r + direction[0], c + direction[1], visit, heights[r][c])

        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols - 1, atlantic, heights[i][cols - 1])

        for j in range(cols):
            dfs(0, j, pacific, heights[0][j])
            dfs(rows - 1, j, atlantic, heights[rows - 1][j])

        result = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])
        return result


class PacificAtlanticWaterFlow:
    heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    x = Solution().pacificAtlantic(heights)
    print(x)
