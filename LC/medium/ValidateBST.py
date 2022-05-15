from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traversal = []
        self.inorder_traversal(root, traversal)
        for i in range(1, len(traversal)):
            if traversal[i] <= traversal[i - 1]:
                return False
        return True

    def inorder_traversal(self, node: TreeNode, result: list):
        if not node:
            return
        self.inorder_traversal(node.left, result)
        result.append(node.val)
        self.inorder_traversal(node.right, result)


class ValidateBinarySearchTree:
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    solution = Solution()
    x = solution.isValidBST(root)
    print(x)
