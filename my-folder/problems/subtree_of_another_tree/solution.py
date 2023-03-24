# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def match_tree(n1: Optional[TreeNode], n2: Optional[TreeNode]):
            if n1 is None and n2 is None:
                return True
            elif n1 is None or n2 is None:
                return False
            elif n1.val != n2.val:
                return False
            else:
                return match_tree(n1.left, n2.left) and match_tree(n1.right, n2.right)

        def search_recurse(node: Optional[TreeNode]):
            if node is None:
                return False
            if match_tree(node, subRoot):
                return True
            elif search_recurse(node.left):
                return True
            elif search_recurse(node.right):
                return True
            return False
        
        return search_recurse(root)