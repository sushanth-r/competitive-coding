from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    target = i - coin
                    dp[i] = min(dp[i], 1 + dp[target])
        return dp[amount] if dp[amount] < float("inf") else -1


class CoinChange:
    coins = list(map(int, input().split()))
    amount = int(input())
    solution = Solution()
    x = solution.coinChange(coins, amount)
    print(x)
