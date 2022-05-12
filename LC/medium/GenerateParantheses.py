from typing import List


def generateParenthesis(n: int) -> List[str]:
    result = []
    generate_parantheses_helper(n, n, "", result)
    return result


def generate_parantheses_helper(left_remaining, right_remaining, pattern, result):
    if left_remaining < 0 or right_remaining < 0 or left_remaining > right_remaining:
        return
    if left_remaining == 0 and right_remaining == 0:
        result.append(pattern)
        return
    generate_parantheses_helper(left_remaining - 1, right_remaining, pattern + "(", result)
    generate_parantheses_helper(left_remaining, right_remaining - 1, pattern + ")", result)


class GenerateParantheses:
    n = int(input())
    print(generateParenthesis(n))
