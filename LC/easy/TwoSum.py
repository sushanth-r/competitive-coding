from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    dictionary = dict()
    for index, num in enumerate(nums):
        complement = target - num
        if complement in dictionary:
            return [dictionary[complement], index]
        dictionary[num] = index
    return [-1, -1]


class TwoSum:
    nums = list(map(int, input().split()))
    target = int(input())
    print(twoSum(nums, target))
