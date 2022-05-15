import collections
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dic = {}
        queue = collections.deque()
        queue.append((root, 0))
        while queue:
            node, cur_height = queue.popleft()
            if node:
                if cur_height not in dic:
                    dic[cur_height] = node.val
                queue.append((node.right, cur_height + 1))
                queue.append((node.left, cur_height + 1))
        return list(dic.values())


class BinaryTreeRightSideView:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    solution = Solution()
    x = solution.rightSideView(root)
    print(x)
