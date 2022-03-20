def generateDocument(characters: str, document: str):
    characters_dictionary = {}
    document_dictionary = {}
    addCharactersToDictionary(characters, characters_dictionary)
    addCharactersToDictionary(document, document_dictionary)

    for key in document_dictionary.keys():
        if key not in characters_dictionary:
            return False
        else:
            if document_dictionary[key] > characters_dictionary[key]:
                return False
    return True


def addCharactersToDictionary(characters: str, dictionary: dict):
    for character in characters:
        if character in dictionary:
            dictionary[character] = dictionary[character] + 1
        else:
            dictionary[character] = 1


class GenerateDocument:
    characters = input()
    document = input()
    print(generateDocument(characters, document))
