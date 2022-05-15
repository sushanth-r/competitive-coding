class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1
        for i in range(2, n + 1):
            temp = first + second
            first = second
            second = temp
        return second


class ClimbingStairs:
    n = int(input())
    solution = Solution()
    x = solution.climbStairs(n)
    print(x)
