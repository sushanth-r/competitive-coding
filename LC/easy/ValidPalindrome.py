def isPalindrome(s: str) -> bool:
    formatted_string = ""
    for character in s:
        if not character.isalnum():
            continue
        formatted_string += character.lower()
    return formatted_string == formatted_string[::-1]


class ValidPalindrome:
    s = input()
    print(isPalindrome(s))
