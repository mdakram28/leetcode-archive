# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = [root]
        ret = []

        i = 0
        while i < len(q):
            ret.append(q[-1].val)
            i_lim = len(q)
            while i < i_lim:
                node = q[i]
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

                i += 1

        return ret