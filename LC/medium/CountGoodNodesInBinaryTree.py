import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        queue = collections.deque()
        queue.append((root, root.val))
        while queue:
            node, maximum = queue.popleft()
            if node:
                if node.val >= maximum:
                    good_nodes += 1
                queue.append((node.left, max(node.val, maximum)))
                queue.append((node.right, max(node.val, maximum)))
        return good_nodes


class CountGoodNodesInBinaryTree:
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    solution = Solution()
    x = solution.goodNodes(root)
    print(x)
