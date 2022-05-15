from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal = []
        self.inorder_traversal(root, traversal)
        return traversal[k - 1]

    def inorder_traversal(self, node: TreeNode, result: list):
        if not node:
            return
        self.inorder_traversal(node.left, result)
        result.append(node.val)
        self.inorder_traversal(node.right, result)


class KthSmallestElementInBST:
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    solution = Solution()
    x = solution.kthSmallest(root, 4)
    print(x)
