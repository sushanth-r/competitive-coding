class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length, s2_length = len(s1), len(s2)
        if s1_length > len(s2):
            return False
        s1_dict = dict()
        s2_dict = dict()
        for i in range(len(s1)):
            s1_dict[s1[i]] = 1 + s1_dict.get(s1[i], 0)
            s2_dict[s2[i]] = 1 + s2_dict.get(s2[i], 0)
        matches = 0
        for i in range(97, 123):
            if s1_dict.get(chr(i), 0) == s2_dict.get(chr(i), 0):
                matches += 1
        left = 0
        for right in range(s1_length, s2_length):
            l_char, r_char = s2[left], s2[right]
            if matches == 26:
                return True
            s2_dict[r_char] = 1 + s2_dict.get(r_char, 0)
            if s1_dict.get(r_char, 0) == s2_dict.get(r_char):
                matches += 1
            elif s1_dict.get(r_char, 0) + 1 == s2_dict.get(r_char):
                matches -= 1

            s2_dict[l_char] -= 1
            if s1_dict.get(l_char, 0) == s2_dict.get(l_char):
                matches += 1
            elif s1_dict.get(l_char, 0) - 1 == s2_dict.get(l_char):
                matches -= 1
            left += 1
        return matches == 26


class PermutationInString:
    s1 = input()
    s2 = input()
    x = Solution().checkInclusion(s1, s2)
    print(x)
