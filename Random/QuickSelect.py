import random
from typing import List


class Solution:
    def kthLargest(self, nums: List[int], k: int) -> int:
        left, right, mid = [], [], []

        pivot = random.choice(nums)

        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else:
                mid.append(num)

        L, M = len(left), len(mid)

        if k <= L:
            return self.kthLargest(left, k)
        elif k > (L + M):
            return self.kthLargest(right, k - (L + M))
        else:
            return mid[0]

    def kthSmallest(self, nums: List[int], k: int) -> int:
        left, right, mid = [], [], []

        pivot = random.choice(nums)

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                mid.append(num)

        L, M = len(left), len(mid)

        if k <= L:
            return self.kthSmallest(left, k)
        elif k > (L + M):
            return self.kthSmallest(right, k - (L + M))
        else:
            return mid[0]


class QuickSelect:
    nums = list(map(int, input().split()))
    k = int(input())
    x = Solution().kthLargest(nums, k)
    y = Solution().kthSmallest(nums, k)
    print(x)
    print(y)
