def maxSubsetSumNoAdjacent(array: list) -> int:
    # O(n) - Time and O(n) - Space
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return max(array[0], array[1])
    dp = [0 for element in array]
    dp[0] = array[0]
    dp[1] = array[1]
    dp[2] = max(dp[1], array[2] + dp[0])
    for index in range(3, len(array)):
        dp[index] = max(array[index] + dp[index - 2], dp[index - 1], array[index] + dp[index - 3])
    return dp[len(array) - 1]


class MaxSubSetSumNoAdjacent:
    input = list(map(int, input().split()))
    print(maxSubsetSumNoAdjacent(input))
