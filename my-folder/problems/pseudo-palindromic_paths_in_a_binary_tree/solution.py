# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        prev = set()
        def dfs(at):
            if at is None: return 0
            if at.val in prev:
                prev.remove(at.val)
            else:
                prev.add(at.val)
            
            if at.left is None and at.right is None:
                ans = 1 if len(prev) <= 1 else 0
            else:
                ans = dfs(at.left) + dfs(at.right)

            if at.val in prev:
                prev.remove(at.val)
            else:
                prev.add(at.val)

            return ans
        
        return dfs(root)