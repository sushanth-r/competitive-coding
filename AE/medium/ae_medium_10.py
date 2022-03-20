def get_inorder_successor(node):
    previous_node = node
    node = node.right
    while node.left is not None:
        previous_node = node
        node = node.left
    return node, previous_node


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        node = self
        previous_node = node
        while node is not None:
            previous_node = node
            if value < node.value:
                node = node.left
            else:
                node = node.right
        node = BST(value)
        if value < previous_node.value:
            previous_node.left = node
        else:
            previous_node.right = node
        return self

    def contains(self, value):
        # Write your code here.
        node = self
        while node is not None:
            if node.value == value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def remove(self, value):
        # Write your code here.
        node = self
        previous_node = node
        while node.value != value:
            previous_node = node
            if value < node.value:
                node = node.left
            else:
                node = node.right
        if node.left is None and node.right is None:
            if value < previous_node.value:
                previous_node.left = None
            else:
                previous_node.right = None
        elif node.left is None:
            if value < previous_node.value:
                previous_node.left = node.right
            elif value > previous_node.value:
                previous_node.right = node.right
            else:
                node.value = node.right.value
                node.left = node.right.left if node.right is not None else None
                node.right = node.right.right if node.right is not None else None
        elif node.right is None:
            if value < previous_node.value:
                previous_node.left = node.left
            elif value > previous_node.value:
                previous_node.right = node.left
            else:
                node.value = node.left.value
                node.left = node.left.left if node.left is not None else None
                node.right = node.left.right if node.left is not None else None
        else:
            inorder_successor_node, temp = get_inorder_successor(node)
            if inorder_successor_node == temp.left:
                temp.left = None
            else:
                temp.right = None
            node.value = inorder_successor_node.value
        return self


class BSTConstruction:
    root = BST(10)
    root.insert(5)
    root.remove(10)
    print(root)
