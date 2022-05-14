from typing import Optional
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            return p.val == q.val

        queue = Queue()
        queue.put([root1, root2])
        while queue.qsize():
            node1, node2 = queue.get()
            if not check(node1, node2):
                return False

            if node1:
                queue.put([node1.left, node2.left])
                queue.put([node1.right, node2.right])
        return True


class SameTree:
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root2 = TreeNode(1)
    solution = Solution()
    x = solution.isSameTree(root1, root2)
    print(x)