class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        r, c = 0, 0
        step = 1
        n = len(grid)
        max_steps = n * n
        while step < max_steps:
            for dr, dc in (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2):
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                if grid[nr][nc] == step:
                    r = nr
                    c = nc
                    break
            else:
                return False
            step += 1
        
        return True