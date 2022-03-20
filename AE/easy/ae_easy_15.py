# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    return breakdownSpecialArray(array, 1)


def breakdownSpecialArray(special_array: list, depth: int):
    product_sum = 0
    for element in special_array:
        if type(element) == int:
            product_sum += element
        elif type(element) == list:
            product_sum += breakdownSpecialArray(element, depth+1)
    return depth * product_sum


class ProductSum:
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    print(productSum(array))
