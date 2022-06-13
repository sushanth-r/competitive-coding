from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(0, 2 * n):
            index = i % n
            while stack and nums[index] > nums[stack[-1]]:
                pop = stack.pop()
                result[pop] = nums[index]
            if index < n:
                stack.append(index)

        return result


class NextGreaterElementII:
    nums = list(map(int, input().split()))
    x = Solution().nextGreaterElements(nums)
    print(x)
