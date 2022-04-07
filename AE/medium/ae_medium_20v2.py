def maxSubsetSumNoAdjacent(array: list) -> int:
    # O(n) - Time and O(1) - Space
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    dp1 = array[0]
    dp2 = max(array[0], array[1])
    for index in range(2, len(array)):
        temp = dp2
        dp2 = max(dp2, array[index] + dp1)
        dp1 = temp
    return dp2


class MaxSubSetSumNoAdjacent:
    input = list(map(int, input().split()))
    print(maxSubsetSumNoAdjacent(input))
