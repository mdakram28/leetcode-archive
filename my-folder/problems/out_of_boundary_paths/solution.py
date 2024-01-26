class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        grid = [[0]*(n+1) for _ in range(m+1)]
        next_grid = [[0]*(n+1) for _ in range(m+1)]
        grid[startRow][startColumn] = 1
        ans = 0
        mod = 10**9 + 7
        for _ in range(maxMove):
            for r in range(m):
                for c in range(n):
                    next_grid[r][c] = grid[r-1][c] + grid[r+1][c] + grid[r][c-1] + grid[r][c+1]
                
            ans = (ans + sum(grid[r][0] + grid[r][n-1] for r in range(m)))%mod
            ans = (ans + sum(grid[0][c] + grid[m-1][c] for c in range(n)))%mod
            grid, next_grid = next_grid, grid
        
        return ans