# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node: Optional[TreeNode], l: list[int]) -> None:
        if node is None:
            return
        self.traverse(node.left, l)
        l.append(node.val)
        self.traverse(node.right, l)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        self.traverse(root, l)
        return l
