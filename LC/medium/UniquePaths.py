class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[m - 1][j] = 1
        for i in range(m):
            dp[i][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if dp[i][j] != 0:
                    continue
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]


class UniquePaths:
    m = int(input())
    n = int(input())
    x = Solution().uniquePaths(m, n)
    print(x)
