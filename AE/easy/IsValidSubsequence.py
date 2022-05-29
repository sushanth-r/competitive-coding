def isValidSubsequence(array, sequence):
    flag = True
    last_index = -1
    for element in sequence:
        if element not in array:
            flag = False
            break
        current_index = array.index(element)
        if current_index <= last_index:
            flag = False
            break
        last_index = current_index - 1
        array.__delitem__(current_index)
    return flag


class IsValidSubSequence:
    array = list(map(int, input().split()))
    sequence = list(map(int, input().split()))
    result = isValidSubsequence(array, sequence)
    print(result)
