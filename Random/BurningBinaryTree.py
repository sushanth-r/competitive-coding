# https://www.geeksforgeeks.org/burn-the-binary-tree-starting-from-the-target-node/
# Given a binary tree and target node. By giving the fire to the target node
# and fire starts to spread in a complete tree. The task is to print the sequence
# of the burning nodes of a binary tree.

# Rules for burning the nodes :
#
# Fire will spread constantly to the connected nodes only.
# Every node takes the same time to burn.
# A node burns only once.
import collections


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def solve(self, root, target) -> None:
        connected = collections.defaultdict(list)

        def traverse(node, parent_node):
            if parent_node:
                connected[node.value].append(parent_node.value)
            if node.left:
                connected[node.value].append(node.left.value)
                traverse(node.left, node)
            if node.right:
                connected[node.value].append(node.right.value)
                traverse(node.right, node)

        traverse(root, None)
        visited = set()
        queue = collections.deque()
        queue.append(target)

        while queue:
            temp = []
            queue_length = len(queue)
            for i in range(queue_length):
                cur = queue.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                temp.append(cur)
                for connected_node in connected[cur]:
                    queue.append(connected_node)
            if temp:
                print(temp)


class BurningBinaryTree:
    root = BinaryTree(12)
    root.left = BinaryTree(13)
    root.right = BinaryTree(10)
    root.right.left = BinaryTree(14)
    root.right.right = BinaryTree(15)
    root.right.left.left = BinaryTree(21)
    root.right.left.right = BinaryTree(24)
    root.right.right.left = BinaryTree(22)
    root.right.right.right = BinaryTree(23)
    target = 14
    Solution().solve(root, target)
