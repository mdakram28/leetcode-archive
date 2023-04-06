class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # on_boundary = False
        def dfs(r, c):
            # nonlocal on_boundary
            if r < 0 or r>=m or c<0 or c>=n:
                # on_boundary = True
                return 0
            if grid[r][c] != 0:
                return 1
            grid[r][c] = 1
            ret = 1
            if dfs(r-1, c) == 0:
                ret = 0
            if dfs(r+1, c) == 0:
                ret = 0
            if dfs(r, c-1) == 0:
                ret = 0
            if dfs(r, c+1) == 0:
                ret = 0
            return ret
        
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    count += dfs(r, c)
                    # if _c == 1:
                        # print(f"Found 1 at {r}, {c}")
                    # count += _c
        
        return count