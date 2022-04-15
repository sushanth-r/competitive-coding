def kadanesAlgorithm(array):
    sub_array_sum, max_sub_array_sum = 0, float("-inf")
    for element in array:
        sub_array_sum = max(sub_array_sum + element, element)
        if sub_array_sum > max_sub_array_sum:
            max_sub_array_sum = sub_array_sum
    return max_sub_array_sum


class KadanesAlgorithm:
    # array = list(map(int, input().split()))
    array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    print(kadanesAlgorithm(array))
