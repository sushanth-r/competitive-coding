from typing import List


class Solution:
    # Time - O(n), Space - O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for index, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict:
                return [index, nums_dict[complement]]
            nums_dict[num] = index


class TwoSum:
    nums = list(map(int, input().split()))
    target = int(input())
    x = Solution().twoSum(nums, target)
    print(x)
