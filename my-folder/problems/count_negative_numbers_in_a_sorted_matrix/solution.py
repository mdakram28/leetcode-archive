class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        c = n-1
        total = 0

        for r in range(m):
            while c >= 0 and grid[r][c] < 0:
                c -= 1
            total += n-1-c
        
        return total