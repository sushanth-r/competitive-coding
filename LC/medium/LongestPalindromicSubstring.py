class Solution:
    def longestPalindrome(self, s: str) -> str:
        left_index = [0]
        right_index = [0]
        longest_palindromic_substring_length = [0]
        for i in range(len(s)):
            # odd palindrome
            self.longest_palindrome_helper(s, i, i, longest_palindromic_substring_length,
                                           left_index, right_index)
            left, right = i, i + 1
            self.longest_palindrome_helper(s, i, i + 1, longest_palindromic_substring_length,
                                           left_index, right_index)

        return s[left_index[0]: right_index[0] + 1]

    def longest_palindrome_helper(self, s, left, right, longest_palindromic_substring_length, left_index,
                                  right_index):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > longest_palindromic_substring_length[0]:
                longest_palindromic_substring_length[0] = right - left + 1
                left_index[0] = left
                right_index[0] = right
            left -= 1
            right += 1


class LongestPalindromicSubstring:
    s = input()
    solution = Solution()
    x = solution.longestPalindrome(s)
    print(x)
