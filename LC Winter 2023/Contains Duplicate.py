from typing import List


class Solution:
    # Time - O(n), Space - O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate_v2(self, nums: List[int]) -> bool:
        nums_map = dict()
        for num in nums:
            if num in nums_map:
                return True
            nums_map[num] = 1
        return False


class ContainsDuplicate:
    nums = list(map(int, input().split()))
    x = Solution().containsDuplicate(nums)
    print(x)
