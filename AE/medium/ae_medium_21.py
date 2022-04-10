def numberOfWaysToMakeChange(n: int, denominations: list) -> int:
    dp = [0 for index in range(0, n+1)]
    dp[0] = 1
    for denomination in denominations:
        for amount in range(1, n+1):
            if denomination <= amount:
                dp[amount] = dp[amount] + dp[amount - denomination]
    return dp[n]


class NumberOfWaysToMakeChange:
    n = int(input())
    denominations = list(map(int, input().split()))
    print(numberOfWaysToMakeChange(n, denominations))
