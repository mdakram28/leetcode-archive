class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        total = sum(matrix[0]) + sum(matrix[r][0] for r in range(1, m))
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c]:
                    matrix[r][c] = min(
                        matrix[r-1][c],
                        matrix[r][c-1],
                        matrix[r-1][c-1]
                    ) + 1
                    total += matrix[r][c]
        # print('\n'.join(map(str, matrix)))
        return total