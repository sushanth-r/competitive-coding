class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(b, e):
            if e == 0:
                return 1
            res = helper(b * b, e // 2)
            return res if e % 2 == 0 else b * res
        result = helper(x, abs(n))
        return result if n > 0 else (1 / result)

    def myPowv2(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = abs(n)
            x = 1 / x
        result = 1
        while n:
            if n % 2 == 1:
                result *= x
            x *= x
            n = n // 2
        return result


class Pow:
    x = float(input())
    n = int(input())
    y = Solution().myPowv2(x, n)
    print(y)
