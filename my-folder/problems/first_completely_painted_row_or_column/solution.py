class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        cr = [n] * m
        cc = [m] * n
        
        pos = {}
        for r in range(m):
            for c in range(n):
                pos[mat[r][c]] = (r, c)
        
        for i, num in enumerate(arr):
            r, c = pos[num]
            cr[r] -= 1
            cc[c] -= 1
            if cr[r] == 0 or cc[c] == 0:
                return i
        