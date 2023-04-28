class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * (n+1) for r in range(n+2)]
        for r1, c1, r2, c2 in queries:
            mat[r1][c1] += 1
            mat[r2+1][c2+1] += 1
            mat[r1][c2+1] -= 1
            mat[r2+1][c1] -= 1
        
        # print('\n'.join(map(str, mat)))
        for r in range(n):
            total = 0
            mat[r].pop()
            for c in range(n):
                total += mat[r][c]
                mat[r][c] = mat[r-1][c] + total
        mat.pop()
        mat.pop()
        return mat