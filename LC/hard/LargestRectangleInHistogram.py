from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        length = len(heights)

        for i, height in enumerate(heights):
            index = i
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                max_area = max(max_area, (i - index) * h)
            stack.append((index, height))

        for i in range(len(stack) - 1, -1, -1):
            max_area = max(max_area, (length - stack[i][0]) * stack[i][1])
        return max_area


class LargestRectangleInHistogram:
    heights = list(map(int, input().split()))
    x = Solution().largestRectangleArea(heights)
    print(x)
