class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        flag = True
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len3 != len1 + len2:
            return False
        dp = [[False for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        dp[len1][len2] = True
        for i in range(len1, -1, -1):
            for j in range(len2, -1, -1):
                if i < len1 and dp[i + 1][j] and s3[i + j] == s1[i]:
                    dp[i][j] = True
                if j < len2 and dp[i][j + 1] and s3[i + j] == s2[j]:
                    dp[i][j] = True
        return dp[0][0]


class InterleavingString:
    s1 = "bbbcc"
    s2 = "bbaccbbbabcacc"
    s3 = "bbbbacbcccbcbabbacc"
    x = Solution().isInterleave(s1, s2, s3)
    print(x)
