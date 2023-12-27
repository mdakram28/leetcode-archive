# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = None
        def getLCA(at):
            nonlocal ans
            if at is None: return 0
            ret = 2 if at == p else 1 if at == q else 0
            ret |= (getLCA(at.left) | getLCA(at.right))
            if ret == 3:
                ans = at
                return 0
            else:
                return ret
        
        getLCA(root)
        return ans
            
            