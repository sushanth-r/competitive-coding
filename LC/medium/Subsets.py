from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            for item in range(len(result)):
                result.append([num] + result[item])

        return result


class Subsets:
    nums = list(map(int, input().split()))
    x = Solution().subsets(nums)
    print(x)
