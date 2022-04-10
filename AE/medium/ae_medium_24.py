def numberOfWaysToTraverseGraph(width: int, height: int) -> int:
    # Space - O(n*m) & Time - O(n*m)
    dp = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        dp[i][width - 1] = 1
    for j in range(width):
        dp[height - 1][j] = 1
    dp[height - 1][width - 1] = 0
    i = height - 2
    while i >= 0:
        j = width - 2
        while j >= 0:
            dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
            j -= 1
        i -= 1
    return dp[0][0]


class NumberOfWaysToTraverseGraph:
    width = int(input())
    height = int(input())
    print(numberOfWaysToTraverseGraph(width, height))
