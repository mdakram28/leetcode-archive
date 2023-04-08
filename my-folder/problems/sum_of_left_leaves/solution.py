# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], is_left = False) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val if is_left else 0
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)