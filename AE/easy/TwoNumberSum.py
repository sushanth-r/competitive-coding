def twoNumberSum(array, targetSum):
    result = list()
    for index, first_element in enumerate(array):
        for secondaryIndex in range(index+1, len(array)):
            second_element = array[secondaryIndex]
            if first_element + second_element == targetSum:
                return [first_element, second_element]

    return result


class TwoNumberSum:
    array = list(map(int, input().split()))
    target_sum = int(input())
    print(array)
    result = twoNumberSum(array, target_sum)
    print(result)
