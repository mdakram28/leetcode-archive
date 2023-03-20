# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findStack(self, node, val, st):
        if node is None:
            return False
        if node.val == val:
            st.append(node)
            return True
        elif self.findStack(node.left, val, st) or self.findStack(node.right, val, st):
            st.append(node)
            return True
        else:
            return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        st_p = []
        st_q = []

        self.findStack(root, p.val, st_p)
        self.findStack(root, q.val, st_q)

        st_p.reverse()
        st_q.reverse()

        # print(list(map(lambda s: s.val, st_p)))
        # print(list(map(lambda s: s.val, st_q)))

        i = 0
        min_len = min(len(st_p), len(st_q))
        while i < min_len and st_p[i] == st_q[i]:
            i += 1
        return st_p[i-1]