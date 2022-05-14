from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.get_tree_data(root)[1]

    def get_tree_data(self, node: TreeNode):
        if node is None:
            return [0, True]
        left, right = self.get_tree_data(node.left), self.get_tree_data(node.right)
        return [(1 + max(left[0], right[0])), (abs(left[0] - right[0]) <= 1 and left[1] and right[1])]


class BalancedBinaryTree:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(5)
    root.right = TreeNode(3)
    solution = Solution()
    x = solution.isBalanced(root)
    print(x)
