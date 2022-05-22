from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = 0
        n = 0
        for num in nums:
            actual_sum += num
            n += 1
        sum_of_n = n * (n + 1) // 2
        return sum_of_n - actual_sum


class MissingNumber:
    nums = list(map(int, input().split()))
    x = Solution().missingNumber(nums)
    print(x)
