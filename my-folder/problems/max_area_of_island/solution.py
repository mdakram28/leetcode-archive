class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_a = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            total = 1
            total += dfs(r-1, c)
            total += dfs(r+1, c)
            total += dfs(r, c-1)
            total += dfs(r, c+1)
            return total
        
        for r in range(m):
            for c in range(n):
                max_a = max(max_a, dfs(r, c))
        
        return max_a