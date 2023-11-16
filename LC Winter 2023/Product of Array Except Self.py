from typing import List


class Solution:
    # Time - O(n), Space - O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1 for _ in nums]
        right_product = [1 for _ in nums]

        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]
        return [left_product[i] * right_product[i] for i in range(len(nums))]


class ProductOfArrayExceptSelf:
    nums = list(map(int, input().split()))
    x = Solution().productExceptSelf(nums)
    print(x)
