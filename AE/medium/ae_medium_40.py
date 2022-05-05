def powerset(array):
    result = [[]]
    for i in range(len(array)):
        for j in range(len(result)):
            subset = result[j]
            result.append(subset + [array[i]])
    return result


class PowerSet:
    array = list(map(int, input().split()))
    print(powerset(array))
