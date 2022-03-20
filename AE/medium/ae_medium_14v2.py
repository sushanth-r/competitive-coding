# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    dictionary = dict()
    dictionary["nodes_visited"] = 0
    reverse_inorder(tree, dictionary, k)
    return dictionary["value"]


def reverse_inorder(node: BST, dictionary: dict, k: int):
    if node is None or dictionary["nodes_visited"] >= k:
        return
    reverse_inorder(node.right, dictionary, k)
    if dictionary["nodes_visited"] < k:
        dictionary["nodes_visited"] += 1
        dictionary["value"] = node.value
        reverse_inorder(node.left, dictionary, k)


class KthLargestBST:
    tree = BST(4)
    tree.left = BST(2)
    tree.left.left = BST(1)
    tree.left.right = BST(3)
    tree.right = BST(6)
    tree.right.left = BST(5)
    tree.right.right = BST(7)
    k = 2
    print(findKthLargestValueInBst(tree, k))
