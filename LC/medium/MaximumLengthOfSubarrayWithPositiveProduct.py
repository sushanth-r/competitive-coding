from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        result = 0
        positive_length, negative_length = 0, 0
        for num in nums:
            if num > 0:
                positive_length, negative_length = 1 + positive_length, \
                                                   1 + negative_length if negative_length > 0 else 0
            elif num < 0:
                positive_length, negative_length = 1 + negative_length if negative_length > 0 else 0, \
                                                   1 + positive_length
            else:
                positive_length = 0
                negative_length = 0
            result = max(result, positive_length)
        return result


class MaximumLengthOfSubarrayWithPositiveProduct:
    nums = list(map(int, input().split()))
    x = Solution().getMaxLen(nums)
    print(x)
