class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0] * len(s)
        last = int(s[len(s) - 1])
        if last != 0:
            dp[len(s) - 1] = 1
        for i in range(len(s) - 2, -1, -1):
            cur = int(s[i])
            two_chars = int(s[i] + s[i + 1])
            if cur == 0:
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if two_chars <= 26:
                    if i != len(s) - 2:
                        dp[i] += dp[i + 2]
                    else:
                        dp[i] += 1
        return dp[0]


class DecodeWays:
    s = input()
    solution = Solution()
    x = solution.numDecodings(s)
    print(x)
