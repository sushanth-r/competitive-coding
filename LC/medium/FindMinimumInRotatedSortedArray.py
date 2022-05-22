from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = float("inf")
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                return min(minimum, nums[left])
            mid = (left + right) // 2
            minimum = min(minimum, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return minimum


class FindMinimumInRotatedSortedArray:
    nums = list(map(int, input().split()))
    x = Solution().findMin(nums)
    print(x)
