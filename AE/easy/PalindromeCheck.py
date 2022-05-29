def isPalindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


class PalindromeCheck:
    string = input()
    print(isPalindrome(string))
