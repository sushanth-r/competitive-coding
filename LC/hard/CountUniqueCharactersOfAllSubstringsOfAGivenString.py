import string


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        occurrences = {c: [-1, -1] for c in string.ascii_uppercase}
        occurrences[s[0]][0] = 0
        prev = 1
        result = 1
        for i in range(1, len(s)):
            c = s[i]
            j, k = occurrences[c]
            curr = prev + (i - j) - (j - k)
            prev = curr
            result += curr
            occurrences[c][1] = occurrences[c][0]
            occurrences[c][0] = i
        return result


class CountUniqueCharactersOfAllSubstringsOfAGivenString:
    s = input()
    x = Solution().uniqueLetterString(s)
    print(x)
