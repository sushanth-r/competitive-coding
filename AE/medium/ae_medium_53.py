def reverseWordsInString(string):
    result = ""
    word = ""
    for character in string:
        if character != " ":
            word += character
        else:
            result = " " + word + result
            word = ""
    result = word + result
    return result


class ReverseWordsInString:
    string = input()
    print(reverseWordsInString(string))
