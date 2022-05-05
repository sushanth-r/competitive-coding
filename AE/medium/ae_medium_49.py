def nextGreaterElement(array):
    result = [-1 for element in array]
    stack = []
    for i in range(2 * len(array)):
        index = i % len(array)
        while len(stack) > 0 and array[stack[-1]] < array[index]:
            result[stack.pop()] = array[index]
        stack.append(index)
    return result


class NextGreaterElement:
    array = list(map(int, input().split()))
    print(nextGreaterElement(array))
