# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSubTree(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is not None and right is not None:
            if left.val != right.val:
                return False
            else:
                return self.checkSubTree(left.left, right.right) and self.checkSubTree(left.right, right.left)
        elif left is not None or right is not None:
            return False
        else:
            return True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkSubTree(root.left, root.right)