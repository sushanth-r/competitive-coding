def longestPalindromicSubstring(string: str):
    temp = ""
    result = ""
    longest_palindrome_length = 0
    for i in range(len(string)):
        temp = ""
        for j in range(i, len(string)):
            temp += string[j]
            if temp[::-1] == temp:
                if len(temp) > longest_palindrome_length:
                    longest_palindrome_length = len(temp)
                    result = temp
    return result


class LongestPalindromicSubString:
    string = input()
    print(longestPalindromicSubstring(string))
