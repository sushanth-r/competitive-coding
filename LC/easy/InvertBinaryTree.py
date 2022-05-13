from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class InvertBinaryTree:
    root = TreeNode(5)
    root.left = TreeNode(6)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(8)
    root.right = TreeNode(9)
    root.right.left = TreeNode(10)
    solution = Solution()
    x = solution.invertTree(root)
    y = 3
