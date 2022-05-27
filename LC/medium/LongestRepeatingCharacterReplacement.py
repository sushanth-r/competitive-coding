class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        highest_frequency = 0
        result = 0
        char_dict = dict()
        for i, c in enumerate(s):
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
            highest_frequency = max(highest_frequency, char_dict[c])

            if (i - left + 1 - highest_frequency) > k:
                char_dict[s[left]] -= 1
                left += 1
            else:
                result = max(result, (i - left) + 1)
        return result


class LongestRepeatingCharacterReplacement:
    s = input()
    k = int(input())
    x = Solution().characterReplacement(s, k)
    print(x)
