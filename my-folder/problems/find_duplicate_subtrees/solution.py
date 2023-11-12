# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        @cache
        def ser(node):
            if node is None: return ""
            return f"{node.val}({ser(node.left)})({ser(node.right)})"
        
        c = defaultdict(int)
        d = {}

        def dfs(node):
            if node is None: return
            s = ser(node)
            d[s] = node
            c[s] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return [d[s] for s, count in c.items() if count > 1]