class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        length = len(s)
        result = roman[s[length - 1]]
        for i in range(length - 2, -1, -1):
            result += roman[s[i]] if roman[s[i + 1]] <= roman[s[i]] else -roman[s[i]]
        return result


class RomanToInteger:
    s = input()
    x = Solution().romanToInt(s)
    print(x)
