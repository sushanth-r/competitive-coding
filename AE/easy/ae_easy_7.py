# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    result = []
    helper(root, 0, result)
    print(result)
    return result


def helper(node: BinaryTree, current_sum: int, result: list):
    if node is not None:
        current_sum += node.value
        if node.left is None and node.right is None:
            result.append(current_sum)
        else:
            if node.left is not None:
                helper(node.left, current_sum, result)
            if node.right is not None:
                helper(node.right, current_sum, result)


class BranchSums:
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.left.right = BinaryTree(5)
    root.left.right.left = BinaryTree(10)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    branchSums(root)
