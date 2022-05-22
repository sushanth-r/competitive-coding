class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            n = n & (n - 1)
            result += 1
        return result


class NumberOf1Bits:
    n = int(input())
    x = Solution().hammingWeight(n)
    print(x)
