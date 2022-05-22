from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = current_min = 1
        res = float("-inf")
        for num in nums:
            prev_max = current_max
            current_max = max(num, num * prev_max, num * current_min)
            current_min = min(num, num * prev_max, num * current_min)
            res = max(res, current_max)
        return res


class MaximumProductSubarray:
    nums = list(map(int, input().split()))
    solution = Solution()
    x = solution.maxProduct(nums)
    print(x)
