class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        cache = [[None]*n for r in range(n-1)] + [matrix[-1]]
        
        def dfs(r, c):
            if c < 0 or c >= n: return float('inf')
            if cache[r][c] is not None: 
                return cache[r][c]
            # prev += matrix[r][c]
            ans = matrix[r][c] + min(
                dfs(r+1, c-1),
                dfs(r+1, c),
                dfs(r+1, c+1)
            )
            cache[r][c] = ans
            return ans
        
        return min(dfs(0, c) for c in range(n))            