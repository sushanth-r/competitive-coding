class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def minHeightBst(array: list):
    mid = (len(array) - 1) // 2
    root = BST(array[mid])
    minHeightBstHelper(array, 0, (len(array) - 1), root)
    return root


def minHeightBstHelper(array: list, minimum: int, maximum: int, tree: BST):
    if minimum <= maximum:
        if minimum < maximum:
            mid = (maximum + minimum) // 2
        else:
            mid = minimum
        if mid != (len(array) - 1) // 2:
            tree.insert(array[mid])
        minHeightBstHelper(array, minimum, mid - 1, tree)

        minHeightBstHelper(array, mid + 1, maximum, tree)
    else:
        return tree


class MinHeightBST:
    array = list(map(int, input().split()))
    tree = minHeightBst(array)
    print(tree)
