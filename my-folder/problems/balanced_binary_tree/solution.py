# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Returns depth
        def dfs(node):
            if not node: return 1
            if not (l := dfs(node.left)) or not (r := dfs(node.right)): return 0
            if abs(l-r) > 1: return 0
            return max(l, r) + 1
        
        return bool(dfs(root))
            