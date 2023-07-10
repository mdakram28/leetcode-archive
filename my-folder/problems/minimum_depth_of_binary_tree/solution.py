# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        q = [root]
        d = 0
        while q:
            next_q = []
            d += 1
            for at in q:
                if at.left is None and at.right is None:
                    return d
                if at.left is not None:
                    next_q.append(at.left)
                if at.right is not None:
                    next_q.append(at.right)
            q = next_q
        return -1