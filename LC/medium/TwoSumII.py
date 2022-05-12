from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] == target:
            break
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1
    return [i + 1, j + 1]


class TwoSumII:
    nums = list(map(int, input().split()))
    target = int(input())
    print(twoSum(nums, target))
