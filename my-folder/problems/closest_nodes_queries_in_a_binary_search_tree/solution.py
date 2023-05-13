# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # sl = SortedList()
        l = [-1]
        def inorder(node):
            if node is None: return
            inorder(node.left)
            l.append(node.val)
            inorder(node.right)
        
        inorder(root)
        sl = SortedList(l)
        l.append(-1)
           
        ans = []
        
        for q in queries:
            i = sl.bisect_left(q)
            if l[i] == q:
                ans.append((q, q))
            else:
                ans.append((l[i-1], l[i]))
        
        
        return ans
            