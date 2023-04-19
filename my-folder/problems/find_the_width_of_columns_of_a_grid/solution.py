class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        
        m = len(grid)
        n = len(grid[0])
        
        ans = []
        for c in range(n):
            width = 0
            for r in range(m):
                width = max(
                    width, 
                    (math.floor(math.log10(abs(grid[r][c]))) + 1 if grid[r][c] else 1) + int(grid[r][c] < 0)
                )
            ans.append(width)
        return ans