from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return -1


class BinarySearch:
    nums = list(map(int, input().split()))
    target = int(input())
    solution = Solution()
    x = solution.search(nums, target)
    print(x)
