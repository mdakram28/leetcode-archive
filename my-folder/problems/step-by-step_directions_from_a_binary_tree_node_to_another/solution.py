# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(node, val, st=[]):
            if node is None: return False
            if node.val == val:
                st.append(node)
                return True
            if dfs(node.left, val, st) or dfs(node.right, val, st): 
                st.append(node)
                return True
            
            return False

        A, B = [], []
        dfs(root, startValue, A)
        dfs(root, destValue, B)
        A.reverse()
        B.reverse()
        # print([n.val for n in A], [n.val for n in B])
        
        i = 0
        while i<len(A) and i<len(B) and A[i] == B[i]:
            i += 1
        
        ret = ["U"] * (len(A)-i)
        i -= 1
        while i < len(B)-1:
            if B[i+1] == B[i].left: ret.append("L")
            elif B[i+1] == B[i].right: ret.append("R")
            i += 1
        
        return ''.join(ret)

        
