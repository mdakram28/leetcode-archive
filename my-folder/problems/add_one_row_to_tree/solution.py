# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def addRow(node, d):
            if node is None: return
            if d == 2:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
            else:
                addRow(node.left, d-1)
                addRow(node.right, d-1)
        
        if depth == 1:
            return TreeNode(val, root, None)

        addRow(root, depth)
        return root