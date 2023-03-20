# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global i
        global ret
        i = 0
        ret = None

        def recurse(node: Optional[TreeNode]):
            global i
            global ret
            if node is None:
                return
            recurse(node.left)
            if i > k:
                return
            i += 1
            if i == k:
                ret = node.val
                return
            recurse(node.right)
            if i > k:
                return
        
        recurse(root)
        return ret