# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        max_length = 0
        def dfs(node, from_left, prev_len):
            nonlocal max_length
            if node is None: return 0
            max_length = max(max_length, prev_len)
            
            if from_left:
                dfs(node.right, False, prev_len+1)
                dfs(node.left, True, 1)
            else:
                dfs(node.left, True, prev_len+1)
                dfs(node.right, False, 1)
        
        dfs(root.left, True, 1)
        dfs(root.right, False, 1)

        return max_length