from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        result = 0

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])
        for i in range(0, len(height)):
            water = min(max_left[i], max_right[i]) - height[i]
            if water > 0:
                result += water
        return result

    def trap_v2(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        max_left, max_right = height[0], height[len(height) - 1]
        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                if (max_left - height[left]) > 0:
                    result += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                if (max_right - height[right]) > 0:
                    result += max_right - height[right]
        return result


class TrappingRainWater:
    height = [4,2,0,3,2,5]
    x = Solution().trap_v2(height)
    print(x)
