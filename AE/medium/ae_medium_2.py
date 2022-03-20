def smallestDifference(array_one: list, array_two: list):
    result = []
    array_one.sort()
    array_two.sort()
    closest_one = array_one[0]
    closest_two = array_two[0]
    closest_absolute_value = abs(closest_one - closest_two)
    current_absolute_value = abs(closest_one - closest_two)
    i, j = 0, 0
    while i < len(array_one) and j < len(array_two):
        first = array_one[i]
        second = array_two[j]
        if first < second:
            current_absolute_value = second - first
            i += 1
        elif first > second:
            current_absolute_value = first - second
            j += 1
        else:
            return [first, second]
        if current_absolute_value < closest_absolute_value:
            closest_absolute_value = current_absolute_value
            closest_one = first
            closest_two = second
    return [closest_one, closest_two]


class SmallestDifference:
    array_one = list(map(int, input().split()))
    array_two = list(map(int, input().split()))
    print(smallestDifference(array_one, array_two))
