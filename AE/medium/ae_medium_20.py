def maxSubsetSumNoAdjacent(array: list) -> int:
    # O(n) - Time and O(n) - Space
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    dp = [0 for element in array]
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])
    for index in range(2, len(array)):
        dp[index] = max(array[index] + dp[index - 2], dp[index - 1])
    return dp[len(array) - 1]


class MaxSubSetSumNoAdjacent:
    input = list(map(int, input().split()))
    print(maxSubsetSumNoAdjacent(input))
