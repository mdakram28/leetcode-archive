# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = defaultdict(list)
        def dfs(at):
            if at.left:
                g[at.left.val].append(at.val)
                g[at.val].append(at.left.val)
                dfs(at.left)
            if at.right:
                g[at.right.val].append(at.val)
                g[at.val].append(at.right.val)
                dfs(at.right)
        dfs(root)
        # print(g)
        def dfs2(at, p):
            ans = 1
            for to in g[at]:
                if to == p: continue
                ans = max(ans, 1 + dfs2(to, at))
            return ans
        
        return dfs2(start, -1)-1


