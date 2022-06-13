from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        length = len(nums)
        target = sum(nums) - x
        if not target:
            return length
        max_subarray_length = -1
        current_sum = left = 0
        for right in range(length):
            current_sum += nums[right]
            while left < length - 1 and current_sum > target:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                subarray_length = right - left + 1
                max_subarray_length = max(max_subarray_length, subarray_length)
        return length - max_subarray_length if max_subarray_length != -1 else -1


class MinimumOperationsToReduceXToZero:
    nums = list(map(int, input().split()))
    x = int(input())
    y = Solution().minOperations(nums, x)
    print(y)
