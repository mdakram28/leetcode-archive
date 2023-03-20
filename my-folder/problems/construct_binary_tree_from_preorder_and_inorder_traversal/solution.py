# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_i = {val: i for i, val in enumerate(inorder)}

        self.pre_i = 0
        
        def subtree(lower, upper):
            if lower == upper:
                return None
            node = TreeNode(preorder[self.pre_i])
            self.pre_i += 1
            in_i = inorder_i[node.val]
            node.left = subtree(lower, in_i)
            node.right = subtree(in_i+1, upper)
            return node
        
        root = subtree(0, len(preorder))
        return root
