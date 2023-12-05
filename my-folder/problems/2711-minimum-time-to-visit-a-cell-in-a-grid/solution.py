class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        mintime = [[float('inf')]*n for _ in range(m)]
        # [(t, (r,c))]
        q = [(0, (0, 0))]
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        while q:
            t, (r,c) = heappop(q)

            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                nt = t+1
                if nt < grid[nr][nc]:
                    wiggle = 2*ceil((grid[nr][nc] - nt)/2)
                    nt += wiggle
                if mintime[nr][nc] <= nt:
                    continue
                mintime[nr][nc] = nt
                heappush(q, (nt, (nr, nc)))
        # print(mintime)
        return mintime[-1][-1]
                
