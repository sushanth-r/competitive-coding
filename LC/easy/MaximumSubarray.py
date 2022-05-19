from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_so_far = sum_so_far = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > sum_so_far and sum_so_far < 0:
                sum_so_far = nums[i]
            else:
                sum_so_far += nums[i]
            if sum_so_far > max_sum_so_far:
                max_sum_so_far = sum_so_far
        return max_sum_so_far


class MaximumSubarray:
    nums = list(map(int, input().split()))
    solution = Solution()
    x = solution.maxSubArray(nums)
    print(x)
