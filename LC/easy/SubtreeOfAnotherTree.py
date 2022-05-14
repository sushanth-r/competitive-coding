from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if not sub_root:
            return True
        if not root:
            return False
        if self.is_same_tree(root, sub_root):
            return True
        else:
            return self.isSubtree(root.left, sub_root) or self.isSubtree(root.right, sub_root)

    def is_same_tree(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
        else:
            return False


class SubtreeOfAnotherTree:
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)
    root2 = TreeNode(4)
    root2.left = TreeNode(1)
    root2.right = TreeNode(2)
    solution = Solution()
    x = solution.isSubtree(root1, root2)
    print(x)
