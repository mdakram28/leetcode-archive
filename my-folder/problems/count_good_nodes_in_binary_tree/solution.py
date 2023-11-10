# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        st = [(root, -10000)]
        ans = 0
        while st:
            at, c = st.pop()
            if at.val >= c:
                ans += 1
            c = max(c, at.val)
            if at.left:
                st.append((at.left, c))
            if at.right:
                st.append((at.right, c))
        
        return ans