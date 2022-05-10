from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    sorted_dictionary = dict()
    for s in strs:
        key = "".join(sorted(s))
        if key in sorted_dictionary:
            sorted_dictionary[key].append(s)
        else:
            sorted_dictionary[key] = [s]
    return list(sorted_dictionary.values())


class GroupAnagrams:
    strings = list(map(str, input().split()))
    print(groupAnagrams(strings))
