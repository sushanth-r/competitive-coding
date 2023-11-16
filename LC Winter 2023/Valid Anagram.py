from typing import List


class Solution:
    # Time - O(max(nlogn, mlogm)), Space - O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        return sorted_s == sorted_t

    def isAnagramv2(self, s: str, t:str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

class ValidAnagram:
    s = str(input())
    t = str(input())
    x = Solution().isAnagramv2(s, t)
    print(x)
