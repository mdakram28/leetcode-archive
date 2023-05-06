class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        onesRow = [0]*m
        onesCol = [0]*n
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    onesRow[r] += 1
                    onesCol[c] += 1
        
        for r in range(m):
            for c in range(n):
                grid[r][c] = 2*onesRow[r] + 2*onesCol[c] - m - n
        
        return grid