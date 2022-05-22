from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


class SingleNumber:
    nums = list(map(int, input().split()))
    x = Solution().singleNumber(nums)
    print(x)
