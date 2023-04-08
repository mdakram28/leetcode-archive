# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        f = collections.defaultdict(int)
        f[0] = 1

        def dfs(node, s):
            if node is None:
                return 0
            
            s += node.val
            f[s] += 1
            ret = dfs(node.left, s) + dfs(node.right, s)
            f[s] -= 1

            return ret + f[s-targetSum]
        
        return dfs(root, 0)