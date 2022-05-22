from typing import List


class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in word_dict:
                chars = s[i:i + len(word)]
                if word == chars:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]


class WordBreak:
    s = input()
    word_dict = list(map(str, input().split()))
    solution = Solution()
    x = solution.wordBreak(s, word_dict)
    print(x)

