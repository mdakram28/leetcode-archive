# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        lca = None
        def dfs(node):
            nonlocal lca
            if node is None: return None

            l = dfs(node.left)
            if lca is not None: return None
            r = dfs(node.right)

            pf = p if node == p or l == p or r == p else None
            qf = q if node == q or l == q or r == q else None

            if pf and qf:
                lca = node
                return None
            else:
                return pf or qf
        
        dfs(root)
        return lca
