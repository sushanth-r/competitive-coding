def moveElementToEnd(array: list, number: int):
    end_of_list = len(array) - 1
    index = 0
    while index < end_of_list:
        if array[index] == number:
            array.append(array.pop(index))
            end_of_list -= 1
        else:
            index += 1
    return array


class MoveElementToEnd:
    array = list(map(int, input().split()))
    number = int(input())
    print(moveElementToEnd(array, number))
