from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            first, second = second, max(nums[i] + first, second)
        return second


class HouseRobber:
    nums = list(map(int, input().split()))
    solution = Solution()
    x = solution.rob(nums)
    print(x)
