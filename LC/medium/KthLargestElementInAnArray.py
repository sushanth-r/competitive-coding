import random
from typing import List


class Solution:
    def findKthLargestv2(self, nums: List[int], k: int) -> int:
        # O(nlogn) - Time, O(1) - Space
        nums.sort(reverse=True)
        return nums[k - 1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quick Select
        pivot = random.choice(nums)
        left, right, mid = [], [], []
        for num in nums:
            if num > pivot:
                left.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                right.append(num)

        left_len, mid_len = len(left), len(mid)

        if k <= left_len:
            return self.findKthLargest(left, k)
        elif k > (left_len + mid_len):
            return self.findKthLargest(right, k - left_len - mid_len)
        else:
            return mid[0]


class KthLargestElementInAnArray:
    nums = list(map(int, input().split()))
    k = int(input())
    x = Solution().findKthLargest(nums, k)
    print(x)
