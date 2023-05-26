# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        @cache
        def height(node):
            if node is None: return 0
            return 1 + height(node.left)


        def last_node(node):
            if node.left is None and node.right is None: return 1
            hl = height(node.left)
            if hl > height(node.right):
                return last_node(node.left)
            else: 
                return 2**(hl-1) + last_node(node.right)

        ln = last_node(root)
        return 2**(height(root)-1) - 1 + last_node(root)

