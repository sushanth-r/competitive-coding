from typing import List


class Solution:
    def binary_search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


class BinarySearch:
    nums = list(map(int, input().split()))
    target = int(input())
    x = Solution().binary_search(nums, target)
    print(x)
