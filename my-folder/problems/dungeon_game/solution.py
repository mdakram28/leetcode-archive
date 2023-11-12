class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        grid = [[0]*n for r in range(m)]
        INF = float('inf')

        def can_reach(h):
            if dungeon[0][0]+h <= 0:
                return False
            grid[0][0] = dungeon[0][0]
            r = 0
            for c in range(1, n):
                grid[r][c] = dungeon[r][c] + grid[r][c-1]
                if grid[r][c]+h <= 0:
                    grid[r][c] = -INF

            c = 0
            for r in range(1, m):
                grid[r][c] = dungeon[r][c] + grid[r-1][c]
                if grid[r][c]+h <= 0:
                    grid[r][c] = -INF
            
            for r in range(1, m):
                for c in range(1, n):
                    grid[r][c] = dungeon[r][c] + max(grid[r-1][c], grid[r][c-1])
                    if grid[r][c]+h <= 0:
                        grid[r][c] = -INF
            
            return grid[-1][-1]+h > 0

        
        lo = 1
        hi = 1-sum(dungeon[r][c] for r in range(m) for c in range(n) if dungeon[r][c] < 0)
        # print(lo, hi)
        while lo < hi:
            mid = (lo+hi)//2
            if can_reach(mid):
                # print(mid, "can reach")
                hi = mid
            else:
                # print(mid, "cannot reach")
                lo = mid+1
        
        return lo


