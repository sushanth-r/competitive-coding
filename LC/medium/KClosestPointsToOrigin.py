import heapq
import math
from typing import List
from queue import Queue


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        points.sort(key=lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2))
        return points[0:k]

    def kClosest_v2(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for i, item in enumerate(points):
            heap.append((item[0] ** 2 + item[1] ** 2, i))
        heapq.heapify(heap)
        while k > 0:
            result.append(points[heapq.heappop(heap)[1]])
            k -= 1
        return result

    def kClosest_v3(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for i, point in enumerate(points):
            heapq.heappush(heap, (-(point[0] ** 2 + point[1] ** 2), i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [points[i] for distance, i in heap]

    def kClosest_v4(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda x: x[0] ** 2 + x[1] ** 2)


class KClosestPointsToOrigin:
    points = [[3,3],[5,-1],[-2,4]]
    k = int(input())
    x = Solution().kClosest_v4(points, k)
    print(x)
