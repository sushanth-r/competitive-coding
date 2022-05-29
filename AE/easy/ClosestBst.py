def findClosestValueInBst(tree, target):
    return helper(tree, target, tree.value)


def helper(node, target, closest):
    if node is None:
        return closest
    else:
        closest = node.value if abs(target - node.value) < abs(target - closest) else closest
        if node.value > target:
            # go left
            return helper(node.left, target, closest)
        elif node.value <= target:
            return helper(node.right, target, closest)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ClosestBst:
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    target = int(input())
    findClosestValueInBst(root, target)
