class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length, cur_length = 0, 0
        char_dict = dict()
        last_duplicate_occurrence = -1
        for i in range(len(s)):
            char = s[i]
            if char not in char_dict or char_dict[char] < last_duplicate_occurrence:
                char_dict[char] = i
                cur_length += 1
                max_length = max(max_length, cur_length)
            else:
                last_duplicate_occurrence = char_dict[char]
                cur_length = i - last_duplicate_occurrence
                char_dict[char] = i
        return max_length


class LongestSubstringWithoutRepeatingCharacters:
    s = input()
    x = Solution().lengthOfLongestSubstring(s)
    print(x)

