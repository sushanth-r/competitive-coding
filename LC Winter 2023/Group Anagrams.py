from typing import List
from collections import defaultdict


class Solution:
    # O(n) - Time, O(n) - Space
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        result = []
        for string in strs:
            sorted_string = "".join(sorted(string))
            str_dict[sorted_string].append(string)
        for key in str_dict:
            result.append(str_dict[key])
        return list(str_dict.values())


class GroupAnagrams:
    strs = list(map(str, input().split()))
    x = Solution().groupAnagrams(strs)
    print(x)
