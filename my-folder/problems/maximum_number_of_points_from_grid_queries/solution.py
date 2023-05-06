from sortedcontainers import SortedList

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        max_val = [[float('inf')] * n for _ in range(m)]
        
        q = [(grid[0][0], 0, 0)]
        max_val[0][0] = grid[0][0]
        
        while q:
            d, r, c = heappop(q)
            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=m or nc<0 or nc>=n: continue
                nd = max(d, grid[nr][nc])
                if nd < max_val[nr][nc]:
                    max_val[nr][nc] = nd
                    heappush(q, (nd, nr, nc))
        
        # print('\n'.join(map(str, max_val)))
        
        ans = [0] * (len(queries)+1)
        sl = SortedList()
        for i, val in enumerate(queries):
            sl.add((val-1, i))
        
        for row in max_val:
            for val in row:
                ans[sl.bisect_left((val, 0))] += 1
        
        # print(sl, ans)
        
        
        ret = [None] * len(queries)
        total = 0
        for val, (_, i) in zip(ans, sl):
            total += val
            ret[i] = total
        
        return ret
        
            
            
            
            
            
            