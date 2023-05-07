# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        def find(at, node, st):
            if at is None: return False
            if at == node or find(at.left, node, st) or find(at.right, node, st): 
                st.append(at)
                return True
            return False
        

        P = []
        Q = []
        find(root, p, P)
        find(root, q, Q)
        P.reverse()
        Q.reverse()
        # print([n.val for n in P], [n.val for n in Q])
        
        i = 0
        lim = min(len(P), len(Q))

        while i < lim and P[i] == Q[i]:
            i += 1
        return P[i-1]