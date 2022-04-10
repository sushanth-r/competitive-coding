def minNumberOfCoinsForChange(n: int, denominations: list) -> int:
    dp = [float("inf") for index in range(0, n+1)]
    dp[0] = 0
    for amount in range(1, n+1):
        for denomination in denominations:
            if denomination <= amount:
                target = amount - denomination
                dp[amount] = min(dp[amount], 1 + dp[target])
    return dp[n] if dp[n] != float("inf") else -1


class MinNumberOfCoinsForChange:
    n = int(input())
    denominations = list(map(int, input().split()))
    print(minNumberOfCoinsForChange(n, denominations))
