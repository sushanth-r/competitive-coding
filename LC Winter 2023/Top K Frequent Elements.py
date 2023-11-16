from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = defaultdict(int)
        for num in nums:
            frequency_dict[num] += 1
        sorted_list = sorted(frequency_dict, key=frequency_dict.get, reverse=True)
        return sorted_list[:k]


class TopKFrequentElements:
    nums = list(map(int, input().split()))
    k = int(input())
    x = Solution().topKFrequent(nums, k)
    print(x)
