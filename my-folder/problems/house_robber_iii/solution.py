# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        not_rob = self.rob(root.left) + self.rob(root.right)

        rob = root.val
        if root.left:
            rob += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            rob += self.rob(root.right.left) + self.rob(root.right.right)
        
        return max(rob, not_rob)