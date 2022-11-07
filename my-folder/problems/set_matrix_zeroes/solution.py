class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rz = 0 in matrix[0]
        cz = False
        for r in matrix:
            if r[0] == 0:
                cz = True
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
                    
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0
        
        if rz:
            for c in range(0, cols):
                matrix[0][c] = 0
        if cz:
            for r in range(0, rows):
                matrix[r][0] = 0
        