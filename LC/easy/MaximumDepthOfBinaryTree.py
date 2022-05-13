from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode], current_depth=0) -> int:
        if root is None:
            return current_depth
        return max(self.maxDepth(root.left, current_depth + 1),
                   self.maxDepth(root.right, current_depth + 1))


class MaximumDepthOfBinaryTree:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.left.left = TreeNode(7)
    solution = Solution()
    x = solution.maxDepth(root)
    print(x)
