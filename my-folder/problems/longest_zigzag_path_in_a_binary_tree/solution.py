# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        @cache
        def dfs(node):
            nonlocal ans
            if node is None: return 0, 0
            ll, lr = dfs(node.left)
            rl, rr = dfs(node.right)
            l = 1 + lr
            r = 1 + rl
            ans = max(ans, l, r)
            return l, r
        
        dfs(root)

        return ans-1
        