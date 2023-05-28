"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        pref = [[0]*(n+1) for _ in range(n+1)]

        def make_node(t, b, l, r):
            tot = pref[b][r] + pref[t][l] - pref[t][r] - pref[b][l]
            if tot == 0 or tot == (b-t)*(r-l):
                return Node(1 if tot!=0 else 0, True, None, None, None, None)

            mlr = (l+r)//2
            mtb = (t+b)//2
            return Node(
                0, False,
                make_node(t, mtb, l, mlr),
                make_node(t, mtb, mlr, r),
                make_node(mtb, b, l, mlr),
                make_node(mtb, b, mlr, r),
            )
        
        for r in range(n):
            for c in range(n):
                pref[r+1][c+1] = (pref[r][c+1] + pref[r+1][c] - pref[r][c]) + grid[r][c]
        
        return make_node(0, n, 0, n)
