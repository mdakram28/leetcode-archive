# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        levels = []
        l = [root]
        nl = []
        while l:
            levels.append([node.val for node in l])
            for node in l:
                if node.left:
                    nl.append(node.left)
                if node.right:
                    nl.append(node.right)
            l = nl
            nl = []
        levels.reverse()
        return levels