from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum // 2
        dp = {0, nums[0]}
        for i in range(1, len(nums)):
            new_dp = set()
            for ele in dp:
                if ele + nums[i] == target:
                    return True
                new_dp.add(ele + nums[i])
                new_dp.add(ele)
            dp = new_dp
        return target in dp


class PartitionEqualSubsetSum:
    nums = list(map(int, input().split()))
    solution = Solution()
    x = solution.canPartition(nums)
    print(x)
