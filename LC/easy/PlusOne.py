from typing import List


class Solution:
    # def plusOne(self, nums: List[int]) -> List[int]:
    #     for i in range(len(nums) - 1, -1, -1):
    #         if nums[i] == 9:
    #             nums[i] = 0
    #         else:
    #             nums[i] += 1
    #             return nums
    #     nums.insert(0, 1)
    #     return nums

    def plusOne(self, nums: List[int]) -> List[int]:
        s = "".join(str(i) for i in nums)
        plus_one = str(int(s) + 1)
        result = []
        for char in plus_one:
            result.append(int(char))
        return result


class PlusOne:
    nums = list(map(int, input().split()))
    solution = Solution()
    x = solution.plusOne(nums)
    print(x)
