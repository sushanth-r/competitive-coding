def maxSubsetSumNoAdjacent(array: list) -> int:
    # O(n) - Time and O(1) - Space
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return max(array[0], array[1])
    dp1 = array[0]
    dp2 = array[1]
    dp3 = max(dp2, array[2] + dp1)
    for index in range(3, len(array)):
        temp = dp3
        dp3 = max(array[index] + dp2, dp3, array[index] + dp1)
        dp1 = dp2
        dp2 = temp
    return dp3


class MaxSubSetSumNoAdjacent:
    input = list(map(int, input().split()))
    print(maxSubsetSumNoAdjacent(input))
