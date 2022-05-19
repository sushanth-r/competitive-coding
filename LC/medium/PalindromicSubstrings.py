class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            odd_palindrome_count = self.palindrome_helper(s, i, i)
            even_palindrome_count = self.palindrome_helper(s, i, i + 1)
            result += odd_palindrome_count + even_palindrome_count
        return result

    def palindrome_helper(self, s, left, right):
        palindrome_count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindrome_count += 1
            left -= 1
            right += 1
        return palindrome_count


class PalindromicSubstrings:
    s = input()
    solution = Solution()
    x = solution.countSubstrings(s)
    print(x)
