class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = []

        m = len(mat)
        n = len(mat[0])
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    mat[r][c] = 1e5
                else:
                    q.append((r, c))
        
        for r, c in q:
            for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
                nr = r + dr
                nc = c + dc
                new_val = mat[r][c] + 1
                if nr >= 0 and nr < m and nc >= 0 and nc < n and mat[nr][nc] > new_val:
                    mat[nr][nc] = new_val
                    q.append((nr, nc))

        return mat