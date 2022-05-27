from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            result = max(result, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result


class ContainerWithMostWater:
    height = [1,8,6,2,5,4,8,3,7]
    x = Solution().maxArea(height)
    print(x)
