def arrayOfProducts(array: list):
    output = [1 for element in range(len(array))]

    left_side_product = 1
    for index in range(len(array)):
        output[index] *= left_side_product
        left_side_product *= array[index]

    right_side_product = 1
    for index in reversed(range(len(array))):
        output[index] *= right_side_product
        right_side_product *= array[index]

    return output


class ArrayOfProducts:
    array = list(map(int, input().split()))
    print(arrayOfProducts(array))
