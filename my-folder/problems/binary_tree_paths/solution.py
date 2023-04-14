# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ret = []
        prev = []
        def dfs(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                prev.append(node.val)
                ret.append('->'.join(map(str, prev)))
                prev.pop()
                return
            prev.append(node.val)
            dfs(node.left)
            dfs(node.right)
            prev.pop()

            
        dfs(root)
        return ret