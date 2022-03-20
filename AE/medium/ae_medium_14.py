# This is an input class. Do not edit.
# O(n) - Time & O(n) - Space where n is the number of nodes in the tree
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder(node: BST, array: list):
    if node is not None:
        inorder(node.left, array)
        array.append(node.value)
        inorder(node.right, array)


def findKthLargestValueInBst(tree, k):
    array = list()
    inorder(tree, array)
    kth_largest_index = len(array) - k
    return array[kth_largest_index]


class KthLargestBST:
    tree = BST(4)
    tree.left = BST(2)
    tree.left.left = BST(1)
    tree.left.right = BST(3)
    tree.right = BST(6)
    tree.right.left = BST(5)
    tree.right.right = BST(7)
    k = 1
    print(findKthLargestValueInBst(tree, k))
