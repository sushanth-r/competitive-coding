def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
    return list(anagrams.values())


class GroupAnagrams:
    words = list(map(str, input().split()))
    print(groupAnagrams(words))
