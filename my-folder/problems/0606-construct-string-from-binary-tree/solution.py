# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        prev = []
        def dfs(node):
            if node is None:
                return
            prev.append(str(node.val))
            if node.right or node.left:
                prev.append('(')
                dfs(node.left)
                prev.append(')')
            
            if node.right is not None:
                prev.append('(')
                dfs(node.right)
                prev.append(')')
        
        dfs(root)
        return ''.join(prev)
