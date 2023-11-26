class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        for r in range(1, m):
            for c in range(n):
                if matrix[r][c] == 1:
                    matrix[r][c] = matrix[r-1][c]+1
            matrix[r-1].sort(reverse=True)
        
        matrix[-1].sort(reverse=True)
        # print(matrix)

        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, (c+1)*(matrix[r][c]))
        
        return ans