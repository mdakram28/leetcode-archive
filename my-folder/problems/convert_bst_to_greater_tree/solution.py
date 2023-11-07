# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        total = 0
        def travel(at):
            if at is None: return
            nonlocal total
            travel(at.right)
            #process
            total += at.val
            at.val = total
            travel(at.left)
        
        travel(root)
        return root