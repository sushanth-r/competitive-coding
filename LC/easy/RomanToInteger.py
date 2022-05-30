class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": (1, 7), "V": (5, 6), "X": (10, 5), "L": (50, 4), "C": (100, 3), "D": (500, 2), "M": (1000, 1)}
        result = 0
        operation = "add"
        for i in range(len(s) - 1, -1, -1):
            result += roman[s[i]][0] if operation == "add" else -roman[s[i]][0]
            if i > 0:
                operation = "add" if roman[s[i - 1]][1] <= roman[s[i]][1] else "subtract"
        return result


class RomanToInteger:
    s = input()
    x = Solution().romanToInt(s)
    print(x)
