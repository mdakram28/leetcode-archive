class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        max_inf = 0xFFFFFFFF
        min_inf = -max_inf

        q = []

        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                if val == 0:
                    grid[r][c] = min_inf
                elif val == 1:
                    grid[r][c] = max_inf
                else:
                    grid[r][c] = 0
                    q.append((r,c))
        
        for r,c in q:
            nval = grid[r][c] + 1
            for dr, dc in (-1,0), (1,0), (0,-1), (0,1):
                nr = r+dr
                nc = c+dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if grid[nr][nc] > nval:
                    grid[nr][nc] = nval
                    q.append((nr,nc))
        
        max_time = max(map(lambda r: max(map(lambda val: max(0, val),r)),grid))
        return max_time if max_time < max_inf else -1
    
