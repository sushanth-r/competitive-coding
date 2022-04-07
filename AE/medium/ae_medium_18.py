# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_inorder_successor(node: BinaryTree):
    temp = node
    while True:
        if temp.left is None:
            return temp
        elif temp.left is not None:
            temp = temp.left


def findSuccessor(tree, node):
    if node.right:
        return find_inorder_successor(node.right)
    else:
        parent_node = node.parent
        if parent_node is None:
            return None
        if parent_node.left == node:
            return parent_node
        else:
            grand_parent_node = parent_node.parent
            if grand_parent_node is None:
                return None
            if grand_parent_node.left == parent_node:
                return grand_parent_node
            else:
                return None


class FindSuccessor:
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.parent = root
    root.right = BinaryTree(3)
    root.right.parent = root
    root.left.left = BinaryTree(4)
    root.left.left.parent = root.left
    root.left.right = BinaryTree(5)
    root.left.right.parent = root.left
    root.left.left.left = BinaryTree(6)
    root.left.left.left.parent = root.left.left
    node = root
    result = findSuccessor(root, node)
    print(result.value)
