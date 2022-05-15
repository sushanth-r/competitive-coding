from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[-1]
        second = cost[-2]
        for i in range(len(cost) - 3, -1, -1):
            first, second = second, min(cost[i] + first, cost[i] + second)
        return min(first, second)


class MinCostClimbingStairs:
    cost = list(map(int, input().split()))
    solution = Solution()
    x = solution.minCostClimbingStairs(cost)
    print(x)
