import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [(s * -1) for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)

            if largest != second_largest:
                heapq.heappush(stones, largest - second_largest)

        return abs(stones[0]) if stones else 0


class LastStoneWeight:
    stones = list(map(int, input().split()))
    x = Solution().lastStoneWeight(stones)
    print(x)
