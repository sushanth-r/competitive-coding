from queue import Queue


def nodeDepths(root):
    result = 0
    depth = 0
    q = Queue()
    q.put({"node": root, "depth": 0})
    while q.qsize() > 0:
        node_info = q.get()
        node = node_info["node"]
        depth = node_info["depth"]
        if node:
            result += depth
            q.put({"node": node.left, "depth": depth + 1})
            q.put({"node": node.right, "depth": depth + 1})
    print(result)
    return result


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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
