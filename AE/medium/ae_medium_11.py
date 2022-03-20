# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree: BST):
    return helper(tree, float("-inf"), float("inf"))


def helper(node: BST, minimum: float, maximum: float):
    if node is None:
        return True
    if node.value < minimum or node.value >= maximum:
        return False
    is_left_valid = helper(node.left, minimum, node.value)
    is_right_valid = helper(node.right, node.value, maximum)
    return is_left_valid and is_right_valid


class ValidateBST:
    root = BST(10)
    root.left = BST(5)
    root.right = BST(15)
    print(validateBst(root))
