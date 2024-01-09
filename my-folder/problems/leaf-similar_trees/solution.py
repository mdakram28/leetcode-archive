# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

        def dfs(at):
            if at.left is None and at.right is None:
                yield at.val
            else:
                if at.left:
                    yield from dfs(at.left)
                if at.right:
                    yield from dfs(at.right)
        return all(a==b for a, b in zip_longest(dfs(root1), dfs(root2)))