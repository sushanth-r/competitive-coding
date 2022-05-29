def firstNonRepeatingCharacter(string):
    dictionary = {}
    for character in string:
        if character not in dictionary:
            dictionary[character] = 1
        else:
            dictionary[character] += 1

    for index, character in enumerate(string):
        if dictionary[character] == 1:
            return index
    return -1


class FirstNonRepeatingCharacter:
    string = input()
    print(firstNonRepeatingCharacter(string))
