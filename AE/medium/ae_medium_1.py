def threeNumberSum(array: list, target_sum: int):
    output = list()
    compliment_dictionary = dict()
    for index in range(len(array)):
        element = array[index]
        compliment = target_sum - element
        compliment_dictionary[compliment] = index

    i = 0
    while i < len(array) - 1:
        j = i + 1
        while j < len(array):
            two_number_sum = array[i] + array[j]
            if two_number_sum in compliment_dictionary:
                index = compliment_dictionary[two_number_sum]
                if index != i and index != j:
                    element = array[index]
                    triplet = [array[i], array[j], element]
                    triplet.sort()
                    if triplet not in output:
                        output.append(triplet)
            j += 1
        i += 1
    sorted_list = sorted(output, key=lambda x: (x[0], x[1]))
    return sorted_list


class ThreeNumberSum:
    dictionary = {
      "array": [12, 3, 1, 2, -6, 5, -8, 6],
      "targetSum": 0
    }
    print(threeNumberSum(dictionary["array"], dictionary["targetSum"]))
