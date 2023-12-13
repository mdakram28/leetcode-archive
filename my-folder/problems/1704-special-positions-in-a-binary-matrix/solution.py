class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        cr = [sum(row) for row in mat]
        cc = [sum(mat[r][c] for r in range(m)) for c in range(n)]
        return sum(int(mat[r][c] == 1 and cr[r]==1 and cc[c]==1) for r in range(m) for c in range(n))
