def factorial(num: int) -> int:
    result = 1
    while num >= 2:
        result *= num
        num -= 1
    return result


def numberOfWaysToTraverseGraph(width: int, height: int) -> int:
    # Space - O(1) & Time - O(n + m)
    numerator = factorial((width - 1) + (height - 1))
    denominator = factorial(width - 1) * factorial(height - 1)
    return numerator // denominator


class NumberOfWaysToTraverseGraph:
    width = int(input())
    height = int(input())
    print(numberOfWaysToTraverseGraph(width, height))