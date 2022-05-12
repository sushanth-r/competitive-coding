from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    result = [0 for _ in temperatures]
    for index, temperature in enumerate(temperatures):
        while stack and stack[-1][0] < temperature:
            element = stack.pop()
            result[element[1]] = index - element[1]
        stack.append((temperature, index))
    return result


class DailyTemperatures:
    temperatures = list(map(int, input().split()))
    print(dailyTemperatures(temperatures))
