class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            matrix[r].append(float('inf'))
        for r in range(m-2, -1, -1):
            for c in range(n):
                matrix[r][c] += min(
                    matrix[r+1][c-1],
                    matrix[r+1][c],
                    matrix[r+1][c+1]
                )
        
        return min(matrix[0])