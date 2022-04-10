def levenshteinDistance(str1, str2):
    # Space - O(m*n), Time - O(m*n)
    dp = [[float("inf") for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    i, j = 0, 0
    while j <= len(str2):
        dp[len(str1)][j] = len(str2) - j
        j += 1
    while i <= len(str1):
        dp[i][len(str2)] = len(str1) - i
        i += 1
    i = len(str1) - 1
    while i >= 0:
        j = len(str2) - 1
        while j >= 0:
            if str1[i] == str2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
            j -= 1
        i -= 1
    return dp[0][0]


class LevenshteinDistance:
    str1 = input()
    str2 = input()
    print(levenshteinDistance(str1, str2))
