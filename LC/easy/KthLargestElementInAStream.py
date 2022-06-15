import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap, self.k = nums, k
        heapq.heapify(nums)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


class KthLargestElementInAStream:
    k = int(input())
    nums = list(map(int, input().split()))
    k = KthLargest(k, nums)
    print(k.add(1))
