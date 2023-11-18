class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        mineffort = [[float('inf')]*n for r in range(m)]

        q = [(0,0,0)]
        mineffort[0][0] = 0

        while q:
            e, r, c = heappop(q)
            for dr,dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=m or nc<0 or nc>=n: continue
                ne = max(e, abs(heights[nr][nc]-heights[r][c]))
                if ne >= mineffort[nr][nc]: continue
                mineffort[nr][nc] = ne
                heappush(q, (ne, nr,nc))
        
        return mineffort[-1][-1]
