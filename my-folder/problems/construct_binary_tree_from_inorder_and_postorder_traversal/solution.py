# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def get_tree(in_slice, post_slice):
            # print(in_slice, post_slice)
            if len(in_slice) == 0:
                return None
            root_val = post_slice[-1]
            i = in_slice.index(root_val)

            return TreeNode(
                root_val, 
                get_tree(in_slice[:i], post_slice[:i]),
                get_tree(in_slice[i+1:], post_slice[i:-1])
            )
        
        return get_tree(inorder, postorder)