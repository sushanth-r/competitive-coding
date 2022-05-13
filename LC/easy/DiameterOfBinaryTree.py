from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def get_depth(node: TreeNode):
            if node is None:
                return 0
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            depth = 1 + max(left_depth, right_depth)
            cur_diameter = left_depth + right_depth
            diameter[0] = max(cur_diameter, diameter[0])
            return depth

        get_depth(root)
        return diameter[0]


class DiameterOfBinaryTree:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    root.right.left.left.left = TreeNode(8)
    root.right.right.right.right = TreeNode(9)
    solution = Solution()
    x = solution.diameterOfBinaryTree(root)
    print(x)
