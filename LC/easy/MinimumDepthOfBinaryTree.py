from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode], current_depth=1) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return current_depth
        left_depth = float("inf") if root.left is None else self.minDepth(root.left, current_depth + 1)
        right_depth = float("inf") if root.right is None else self.minDepth(root.right, current_depth + 1)
        return min(left_depth, right_depth)


class MinimumDepthOfBinaryTree:
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    root.right.right.right.right = TreeNode(6)
    solution = Solution()
    x = solution.minDepth(root)
    print(x)
