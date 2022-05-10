import collections


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


class ValidAnagram:
    str1 = input()
    str2 = input()
    print(isAnagram(str1, str2))
