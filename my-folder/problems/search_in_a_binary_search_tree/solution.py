# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def find_val(node):
            nonlocal val
            if node is None: return None
            if node.val == val:
                return node
            else:
                return find_val(node.left) or find_val(node.right)
        
        return find_val(root)