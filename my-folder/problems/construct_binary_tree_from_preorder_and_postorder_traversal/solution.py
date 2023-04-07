# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        node = TreeNode(preorder[0])
        if len(preorder) >= 2:
            left_val = preorder[1]
            left_len = postorder.index(left_val) + 1
            node.left = self.constructFromPrePost(preorder[1: 1+left_len], postorder[:left_len])
            node.right = self.constructFromPrePost(preorder[1+left_len:], postorder[left_len:-1])

        return node