def minimumCharactersForWords(words):
    dictionary = {}
    result = []
    for word in words:
        for letter in word:
            if letter not in dictionary:
                dictionary[letter] = 1
            else:
                if word.count(letter) > dictionary[letter]:
                    dictionary[letter] = word.count(letter)
    for letter in dictionary:
        occurrence = dictionary[letter]
        while occurrence > 0:
            result.append(letter)
            occurrence -= 1
    return result


class MinimumCharactersForWords:
    words = list(map(str, input().split()))
    print(minimumCharactersForWords(words))
