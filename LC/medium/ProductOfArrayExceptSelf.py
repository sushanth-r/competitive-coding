from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    result = [0 for _ in nums]
    product = 1
    for i, num in enumerate(nums):
        result[i] = product
        product *= num
    product = 1
    for i in range(len(nums) -1, -1, -1):
        result[i] *= product
        product *= nums[i]
    return result


class ProductOfArrayExceptSelf:
    nums = list(map(int, input().split()))
    print(productExceptSelf(nums))
