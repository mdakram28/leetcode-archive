# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []
        prev_vals = []
        prev_sum = 0
        def dfs(node):
            nonlocal prev_sum
            if node.left is None and node.right is None:
                if prev_sum+node.val == targetSum:
                    ret.append([*prev_vals, node.val])
            else:
                prev_sum += node.val
                prev_vals.append(node.val)
                node.left and dfs(node.left)
                node.right and dfs(node.right)
                prev_sum -= node.val
                prev_vals.pop()
        
        root and dfs(root)
        return ret