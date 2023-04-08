# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_sum = 0

        def max_depth(node):
            nonlocal max_sum
            if node is None:
                return 0
            else:
                ld = max_depth(node.left)
                rd = max_depth(node.right)
                max_sum = max(max_sum, ld+rd)
                return max(ld, rd) + 1
        max_depth(root)
        return max_sum