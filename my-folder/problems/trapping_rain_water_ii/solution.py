class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        INF = float('inf')

        height = [[INF]*n for _ in range(m)]
        height[0] = [*heightMap[0]]
        height[m-1] = [*heightMap[m-1]]

        q = []

        for r in range(m):
            q.append((heightMap[r][0], r, 0))
            height[r][0] = heightMap[r][0]
            q.append((heightMap[r][n-1], r, n-1))
            height[r][n-1] = heightMap[r][n-1]
        
        for c in range(1, n-1):
            q.append((heightMap[0][c], 0, c))
            q.append((heightMap[m-1][c], m-1, c))

        heapq.heapify(q)
        
        while q:
            h, r, c = heapq.heappop(q)
            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=m or nc<0 or nc>=n:
                    continue
                nh = max(heightMap[nr][nc], h)
                if nh < height[nr][nc]:
                    height[nr][nc] = nh
                    heapq.heappush(q, (nh, nr, nc))
        
        return sum( 
            sum(height[r][c]-heightMap[r][c] for c in range(1, n-1) ) 
            for r in range(1, m-1)
        )

