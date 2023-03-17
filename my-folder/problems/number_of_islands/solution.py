class Solution:
    def clearIsland(self, grid, r, c):
        grid[r][c] = '#'
        q = [(r, c)]
        for r, c in q:
            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr = r + dr
                nc = c + dc
                if nr >= 0 and nr < self.m and nc >= 0 and nc < self.n and grid[nr][nc] == '1':
                    q.append((nr, nc))
                    grid[nr][nc] = '#'
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        count = 0
        for r in range(self.m):
            for c in range(self.n):
                if grid[r][c] != '1':
                    continue
                count += 1
                self.clearIsland(grid, r, c)
        return count