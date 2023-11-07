class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        r0 = False
        c0 = False

        for r in range(1, m):
            if matrix[r][0] == 0:
                c0 = True
        
        for c in range(1, n):
            if matrix[0][c] == 0:
                r0 = True
        
        if matrix[0][0] == 0:
            r0 = True
            c0 = True

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, m):
            if matrix[r][0] == 0:
                for c in range(n):
                    matrix[r][c] = 0
        
        for c in range(1, n):
            if matrix[0][c] == 0:
                for r in range(m):
                    matrix[r][c] = 0
        
        if r0:
            for c in range(n):
                matrix[0][c] = 0

        if c0:
            for r in range(m):
                matrix[r][0] = 0