def getPermutations(array):
    result = []

    if len(array) == 1:
        return [array[:]]

    for i in range(len(array)):
        element = array.pop(0)
        permutations = getPermutations(array)
        for permutation in permutations:
            permutation.append(element)
        result.extend(permutations)
        array.append(element)
    return result


class Permutations:
    array = list(map(int, input().split()))
    print(getPermutations(array))
