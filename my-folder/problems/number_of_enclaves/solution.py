class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        border = sum(map(sum, grid))

        def fill(r, c):
            nonlocal border
            if r < 0 or r>= m or c<0 or c >= n or grid[r][c] != 1:
                return
            grid[r][c] = 0
            border -= 1
            fill(r-1, c)
            fill(r+1, c)
            fill(r, c-1)
            fill(r, c+1)
        
        r = 0
        for c in range(n-1):
            fill(r, c)
        c = n-1
        for r in range(m-1):
            fill(r, c)
        r = m-1
        for c in range(1, n):
            fill(r, c)
        c = 0
        for r in range(1, m):
            fill(r, c)
        
        return border