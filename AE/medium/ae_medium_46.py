def balancedBrackets(string: str):
    stack = []
    for character in string:
        if character == '(' or character == '{' or character == '[':
            stack.append(character)
        elif character == ')' or character == '}' or character == ']':
            if len(stack) != 0:
                popped_character = stack.pop()
                if character == ')' and popped_character != '(':
                    return False
                elif character == ']' and popped_character != '[':
                    return False
                elif character == '}' and popped_character != '{':
                    return False
            else:
                return False
    return len(stack) == 0


class BalancedBrackets:
    string = input()
    print(balancedBrackets(string))
