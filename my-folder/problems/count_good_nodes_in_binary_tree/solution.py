# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, node: TreeNode, max_val = -float('inf')) -> int:
        if not node: return 0
        ret = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)
        return ret + self.goodNodes(node.left, max_val) + self.goodNodes(node.right, max_val)