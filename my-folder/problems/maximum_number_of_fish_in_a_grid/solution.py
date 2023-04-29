class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        visited = [[False]*n for r in range(m)]
        
        def dfs(r, c):
            if r < 0 or r>= m or c<0 or c>=n or visited[r][c] or grid[r][c] == 0:
                return 0
            visited[r][c] = True
            return dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1) + grid[r][c]
        
        max_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] and not visited[r][c]:
                    max_count = max(max_count, dfs(r, c))
                    
        return max_count