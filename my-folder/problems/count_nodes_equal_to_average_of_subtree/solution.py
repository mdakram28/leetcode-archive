# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(at):
            nonlocal ans
            if at is None: return (0, 0)
            t1, c1 = dfs(at.left)
            t2, c2 = dfs(at.right)
            t = at.val + t1 + t2
            c = 1 + c1 + c2
            # print(at.val, t, c)
            if t//c == at.val:
                # print("Added", at.val)
                ans += 1
            return (t, c)

        dfs(root)
        return ans


