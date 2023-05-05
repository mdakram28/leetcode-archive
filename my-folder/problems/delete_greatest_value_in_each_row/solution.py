class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for r in grid:
            r.sort()
        
        total = 0
        for c in range(n):
            total += max(grid[r][c] for r in range(m))
        
        return total