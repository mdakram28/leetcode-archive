class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        r = 0
        for c in range(1, n):
            grid[r][c] += grid[r][c-1]
        c = 0
        for r in range(1, m):
            grid[r][c] += grid[r-1][c]

        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        
        return grid[-1][-1]
