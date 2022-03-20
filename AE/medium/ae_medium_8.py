# O(n) - Time & O(n) - Space
def firstDuplicateValue(array: list):
    count_dict = {}
    for number in array:
        if number in count_dict:
            return number
        count_dict[number] = 1
    return -1


class FirstDuplicateValue:
    array = list(map(int, input().split()))
    print(firstDuplicateValue(array))
