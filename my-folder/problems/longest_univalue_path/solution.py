# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def longest(node, val):
            nonlocal ans
            if node is None: return 0
            left = longest(node.left, node.val)
            right = longest(node.right, node.val)
            ans = max(ans, 1 + left + right)

            if node.val == val:
                return max(left, right) + 1
            else:
                return 0
        
        longest(root, 0)
        return max(ans-1, 0)