from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []
    operators = ("+", "-", "*", "/")
    for token in tokens:
        if token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            else:
                result = int(operand1 / operand2)
            stack.append(result)
        else:
            stack.append(int(token))
    return stack[0]


class EvaluateReversePolishNotation:
    tokens = list(map(str, input().split()))
    print(evalRPN(tokens))
