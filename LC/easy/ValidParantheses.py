def isValid(s: str) -> bool:
    stack = []
    parantheses_dictionary = {"{": "}", "[": "]", "(": ")"}
    for character in s:
        if character == '(' or character == '[' or character == '{':
            stack.append(character)
        else:
            if not stack:
                return False
            popped_character = stack.pop()
            if parantheses_dictionary[popped_character] == character:
                continue
            return False
    return len(stack) == 0


class ValidParantheses:
    s = input()
    print(isValid(s))
