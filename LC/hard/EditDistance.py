class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1), len(word2)

        dp = [[0 for _ in range(cols + 1)] for i in range(rows + 1)]

        for i in range(rows + 1):
            dp[i][cols] = rows - i
        for j in range(cols + 1):
            dp[rows][j] = cols - j
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]


class EditDistance:
    word1 = input()
    word2 = input()
    x = Solution().minDistance(word1, word2)
    print(x)
