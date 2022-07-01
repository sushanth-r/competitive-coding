from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]
        return sum(abs(num - mid) for num in nums)


class MinimumMovesToEqualArrayElementsII:
    nums = list(map(int, input().split()))
    x = Solution().minMoves2(nums)
    print(x)
