# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree: BinaryTree):
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


class InvertBinaryTree:
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    # tree.left.left = BinaryTree(4)
    # tree.left.left.left = BinaryTree(8)
    # tree.left.left.right = BinaryTree(9)
    # tree.left.right = BinaryTree(5)
    # tree.right = BinaryTree(3)
    # tree.right.left = BinaryTree(6)
    # tree.right.right = BinaryTree(7)
    inverted_tree = invertBinaryTree(tree)
    print(inverted_tree)
