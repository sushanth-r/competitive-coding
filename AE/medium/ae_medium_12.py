class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inOrderTraverse(tree: BST, array: list):
    if tree:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree: BST, array: list):
    if tree:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree: BST, array: list):
    if tree:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array


class BSTTraversal:
    root = BST(10)
    root.left = BST(5)
    root.right = BST(15)
    array = list()
    print(inOrderTraverse(root, array))
