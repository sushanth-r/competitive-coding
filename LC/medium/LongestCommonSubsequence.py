class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        rows, cols = len(text1), len(text2)
        dp = [[0 for j in range(cols + 1)] for i in range(rows + 1)]

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]


class LongestCommonSubsequence:
    text1 = input()
    text2 = input()
    x = Solution().longestCommonSubsequence(text1, text2)
    print(x)
