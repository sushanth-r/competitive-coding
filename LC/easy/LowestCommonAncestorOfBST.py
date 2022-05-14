class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val <= q.val:
            min_val, max_val = p.val, q.val
        else:
            min_val, max_val = q.val, p.val
        return self.lowest_common_ancestor_helper(root, min_val, max_val)

    def lowest_common_ancestor_helper(self, node: TreeNode, min_val, max_val):

        if min_val <= node.val <= max_val:
            return node

        elif max_val < node.val:
            return self.lowest_common_ancestor_helper(node.left, min_val, max_val)

        elif min_val > node.val:
            return self.lowest_common_ancestor_helper(node.right, min_val, max_val)


class LowestCommonAncestorOfBST:
    root = TreeNode(6)
    p = root.left = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    q = root.right.right = TreeNode(9)
    solution = Solution()
    x = solution.lowestCommonAncestor(root, p, q)
    print(x.val)
