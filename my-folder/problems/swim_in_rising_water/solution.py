class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        INF = float('inf')
        route_max = [[INF]*n for _ in range(n)]

        route_max[0][0] = grid[0][0]
        q = [(grid[0][0], 0, 0)]

        while q:
            t, r, c = heapq.heappop(q)
            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                nt = max(grid[nr][nc], t)
                if route_max[nr][nc] > nt:
                    route_max[nr][nc] = nt
                    heapq.heappush(q, (nt, nr, nc))
        
        return route_max[-1][-1]
                