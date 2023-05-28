class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        topLeft = [([None]*n) for r in range(m)]
        
        r = 0
        for c in range(n):
            topLeft[r][c] = set()
        
        c = 0
        for r in range(m):
            topLeft[r][c] = set()
        
        for r in range(1, m):
            for c in range(1, n):
                topLeft[r][c] = topLeft[r-1][c-1].copy()
                topLeft[r][c].add(grid[r-1][c-1])
                
        
        bottomRight = [([None]*n) for r in range(m)]
        
        r = m-1
        for c in range(n):
            bottomRight[r][c] = set()
        
        c = n-1
        for r in range(m):
            bottomRight[r][c] = set()
        
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                bottomRight[r][c] = bottomRight[r+1][c+1].copy()
                bottomRight[r][c].add(grid[r+1][c+1])
        
        
        for r in range(m):
            for c in range(n):
                grid[r][c] = abs(len(topLeft[r][c]) - len(bottomRight[r][c]))
        
        return grid
                