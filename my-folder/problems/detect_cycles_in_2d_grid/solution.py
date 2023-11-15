class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        q = []

        def iscycle(r, c, pr, pc, char, visited):
            grid[r][c] = visited
            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n: continue
                if nr == pr and nc == pc: continue
                if grid[nr][nc] == visited: return True
                if grid[nr][nc] != char: continue
                if iscycle(nr, nc, r, c, char, visited): return True
            return False
        
        g = 0
        for r, c in product(range(m), range(n)):
            if isinstance(grid[r][c], str):
                g += 1
                if iscycle(r, c, None, None, grid[r][c], g):
                    return True
        
        return False
