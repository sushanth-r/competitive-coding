# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def populate_tree_list(node: BinaryTree, tree_list: list):
    if not node:
        return
    tree_list.append(node)
    populate_tree_list(node.left, tree_list)
    populate_tree_list(node.right, tree_list)


def get_tree_height(node: BinaryTree, current_height: int):
    if not node:
        return current_height
    return max(get_tree_height(node.left, current_height + 1), get_tree_height(node.right, current_height + 1))


def heightBalancedBinaryTree(tree: BinaryTree):
    # Write your code here.
    node_list = []
    populate_tree_list(tree, node_list)
    for node in node_list:
        left_height = get_tree_height(node.left, 0) if node.left else 0
        right_height = get_tree_height(node.right, 0) if node.right else 0
        difference = abs(left_height - right_height)
        if difference > 1:
            return False
    return True


class HeightBalancedBinaryTree:
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.right = BinaryTree(6)
    root.left.right.left = BinaryTree(7)
    root.left.right.right = BinaryTree(8)
    print(heightBalancedBinaryTree(root))
