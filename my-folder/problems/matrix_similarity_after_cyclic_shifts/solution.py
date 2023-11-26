class Solution:
    def areSimilar(self, matrix: List[List[int]], k: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # if n%2 != 0: return False
        
        m2 = [[0]*n for r in range(m)]
        
        for r in range(m):
            for c in range(n):
                if r%2 == 0:
                    m2[r][(c-k)%n] = matrix[r][c]
                else:
                    m2[r][(c+k)%n] = matrix[r][c]
        
        return m2 == matrix
        
            