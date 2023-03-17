# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, node: Optional[TreeNode], lower = -(1<<32), upper=(1<<32)) -> bool:
        if node is None:
            return True 
        if node.val <= lower or node.val >= upper:
            return False
        return self.isValidBST(node.left, lower, node.val) and self.isValidBST(node.right, node.val, upper)