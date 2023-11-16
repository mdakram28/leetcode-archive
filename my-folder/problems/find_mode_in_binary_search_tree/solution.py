# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        prev = None
        c = 0
        ans = set()
        maxc = 0
        def dfs(at):
            if at is None: return
            dfs(at.left)
            
            nonlocal prev, c, ans, maxc
            if prev == at.val:
                c += 1
            else:
                prev = at.val
                c = 1
                
            if c > maxc:
                ans.clear()
                ans.add(at.val)
                maxc = c
            elif c == maxc:
                ans.add(at.val)

            dfs(at.right)
        
        dfs(root)
        return ans