# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        # Return (isbst, maxval, minval, total)
        def dfs(at):
            isbst = True
            maxval = minval = total = at.val
            if at.left:
                ret = dfs(at.left)
                if not ret[0]:
                    isbst = False
                if ret[1] >= at.val:
                    isbst = False
                maxval = max(maxval, ret[1])
                minval = min(minval, ret[2])
                total += ret[3]
            
            if at.right:
                ret = dfs(at.right)
                if not ret[0]:
                    isbst = False
                if ret[2] <= at.val:
                    isbst = False
                maxval = max(maxval, ret[1])
                minval = min(minval, ret[2])
                total += ret[3]
            if isbst:
                nonlocal ans
                ans = max(ans, total)
            # print(at.val, (isbst, maxval, minval, total))
            return (isbst, maxval, minval, total)
        
        dfs(root)
        return ans