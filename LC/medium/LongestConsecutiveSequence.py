from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums = set(nums)
    longest_consecutive_sequence = 0
    for ind, ele in enumerate(nums):
        current_consecutive_sequence = 1
        if (ele - 1) in nums:
            continue
        while (ele + 1) in nums:
            current_consecutive_sequence += 1
            ele += 1
        longest_consecutive_sequence = max(longest_consecutive_sequence, current_consecutive_sequence)
    return longest_consecutive_sequence


class LongestConsecutiveSequence:
    nums = list(map(int, input().split()))
    print(longestConsecutive(nums))
