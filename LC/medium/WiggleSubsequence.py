from typing import List


class Solution:
    # I = Increasing, D = Decreasing
    def wiggleMaxLength(self, nums: List[int]) -> int:
        max_length = 1
        array_length = len(nums)

        if array_length == 1:
            return 1

        length = 1
        prev = "X"

        for i in range(1, array_length):
            if nums[i] > nums[i - 1]:
                if prev != "I":
                    length += 1
                    prev = "I"

            elif nums[i] < nums[i - 1]:
                if prev != "D":
                    length += 1
                    prev = "D"
        return length


class WiggleSubsequence:
    nums = [1, 0, 0]
    x = Solution().wiggleMaxLength(nums)
    print(x)
