class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])

        inside = True
        def bfs(r, c):
            nonlocal inside
            if r<0 or r>=m or c<0 or c>=n or grid2[r][c] == 0:
                return
            grid2[r][c] = 0
            if grid1[r][c] == 0:
                inside = False
            bfs(r-1, c)
            bfs(r+1, c)
            bfs(r, c-1)
            bfs(r, c+1)
        
        count = 0
        for r in range(m):
            for c in range(n):
                if grid2[r][c]:
                    inside = True
                    bfs(r, c)
                    if inside:
                        count += 1
        
        return count