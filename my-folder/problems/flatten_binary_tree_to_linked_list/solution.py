# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def get_ht(node: TreeNode):
            head, tail = node, node
            if node.right is not None:
                right_h, right_t = get_ht(node.right)
                tail = right_t
            if node.left is not None:
                left_h, left_t = get_ht(node.left)
                left_t.right = node.right
                node.right = left_h
                node.left = None
                if node is tail:
                    tail = left_t
            return head, tail

        if root is not None:
            get_ht(root)