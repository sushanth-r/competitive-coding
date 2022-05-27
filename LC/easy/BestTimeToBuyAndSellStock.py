from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        list1 = [0] * len(prices)

        left_min = float("inf")
        for i in range(len(prices)):
            left_min = min(left_min, prices[i])
            list1[i] = left_min

        right_max = 0
        for i in range(len(prices) - 1, -1, -1):
            right_max = max(right_max, prices[i])
            list1[i] = right_max - list1[i]

        result = 0
        for ele in list1:
            result = max(result, ele)
        return result

    def maxProfitv2(self, prices: List[int]) -> int:
        result = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            result = max(result, (prices[right] - prices[left]))
        return result


class BestTimeToBuyAndSellStock:
    prices = [7,1,5,3,6,4]
    x = Solution().maxProfitv2(prices)
    print(x)
