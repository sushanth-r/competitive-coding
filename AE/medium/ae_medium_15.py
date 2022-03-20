# Time - O(nlogn) & Space - O(n)
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        node = self
        parent_node = node
        while node:
            parent_node = node
            if value < node.value:
                node = node.left
            else:
                node = node.right
        node = BST(value)
        if value < parent_node.value:
            parent_node.left = node
        else:
            parent_node.right = node
        return self


def reconstructBst(array: list):
    root = BST(array[0])
    for index in range(1, len(array)):
        root.insert(array[index])
    return root


class ReconstructBST:
    array = list(map(int, input().split()))
    tree = reconstructBst(array)
    print(tree)
