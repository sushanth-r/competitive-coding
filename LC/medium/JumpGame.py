from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target_index = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target_index:
                target_index = i

        return target_index == 0


class JumpGame:
    nums = list(map(int, input().split()))
    x = Solution().canJump(nums)
    print(x)
