from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        free_pass = 0
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                continue
            if free_pass == 1:
                return False
            free_pass += 1
            nums[i - 1] = nums[i]
            if i > 1 and nums[i - 2] > nums[i - 1]:
                return False
        return True


class NonDecreasingArray:
    nums = list(map(int, input().split()))
    x = Solution().checkPossibility(nums)
    print(x)
