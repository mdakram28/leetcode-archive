class Solution:
    def shortestPathBinaryMatrix(self, dist: List[List[int]]) -> int:
        n = len(dist)
        end = (n-1, n-1)
        def h(r, c):
            dx = abs(r - end[0])
            dy = abs(c - end[1])

            return (dx + dy) + (- 1) * min(dx, dy)

        if dist[0][0] == 1 or dist[-1][-1] == 1: return -1
        # dist = [[float('inf')]*n for r in range(n)]
        for r in range(n):
            for c in range(n):
                if dist[r][c]==0:
                    dist[r][c] = float('inf')
                else:
                    dist[r][c] = 0

        q = [(h(0, 0), 1, 0, 0)]
        dist[0][0] = 1

        while q:
            _, d, r, c = heapq.heappop(q)
            d += 1
            for dr in -1, 0, 1:
                for dc in -1, 0, 1:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nr>=n or nc<0 or nc>=n: continue
                    if dist[nr][nc] > d:
                        dist[nr][nc] = d
                        heapq.heappush(q, (h(nr, nc), d, nr, nc))
        # print('\n'.join(map(str, dist)))
        ret = dist[-1][-1]
        return ret if ret != float('inf') else -1