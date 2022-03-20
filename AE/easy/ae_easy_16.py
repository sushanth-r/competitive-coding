def binarySearch(array, target):
    high = len(array)
    low = 0
    while low < high:
        mid = int((low + high)/2)
        if array[mid] > target:
            high = mid
        elif array[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1


class BinarySearch:
    dict1 = {
      "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
      "target": 33
    }
    print(binarySearch(dict1["array"], dict1["target"]))
