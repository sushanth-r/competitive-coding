from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])
        return max(self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))

    def rob_helper(self, nums: list) -> int:
        first, second = 0, 0
        for i in range(len(nums)):
            first, second = second, max(first + nums[i], second)
        return second


class HouseRobberII:
    nums = list(map(int, input().split()))
    solution = Solution()
    x = solution.rob(nums)
    print(x)
