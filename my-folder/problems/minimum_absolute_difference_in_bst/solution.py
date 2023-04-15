# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        prev_num = -float('inf')
        min_diff = float('inf')
        def bfs(node):
            nonlocal prev_num, min_diff
            if node is None:
                return            
            bfs(node.left)
            min_diff = min(min_diff, node.val - prev_num)
            prev_num = node.val
            bfs(node.right)
        
        bfs(root)
        return min_diff