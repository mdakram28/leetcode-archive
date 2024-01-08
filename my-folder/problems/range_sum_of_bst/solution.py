# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = deque([root])
        total = 0
        while q:
            at = q.popleft()
            if at.val < low:
                if at.right:
                    q.append(at.right)
            elif at.val > high:
                if at.left:
                    q.append(at.left)
            else:
                total += at.val
                if at.left:
                    q.append(at.left)
                if at.right:
                    q.append(at.right)

        return total
        