# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None: return 0
        ret = root.val if low <= root.val <= high else 0
        if root.val <= low:
            ret += self.rangeSumBST(root.right, low, high)
        elif root.val >= high:
            ret += self.rangeSumBST(root.left, low, high)
        else:
            ret += self.rangeSumBST(root.left, low, high)
            ret += self.rangeSumBST(root.right, low, high)
        return ret