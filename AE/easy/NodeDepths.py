from functools import reduce


def nodeDepths(root):
    current_depth = -1
    sum_list = []
    helper(root, current_depth, sum_list)
    result = reduce((lambda x, y: x+y), sum_list)
    return result


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def helper(node: BinaryTree, current_depth: int, sum_list: []):
    current_depth += 1
    sum_list.append(current_depth)
    if node.left is not None:
        helper(node.left, current_depth, sum_list)
    if node.right is not None:
        helper(node.right, current_depth, sum_list)
    return


class NodeDepths:
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    nodeDepths(root)
