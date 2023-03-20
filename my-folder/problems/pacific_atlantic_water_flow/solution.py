

from queue import Queue

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        p_reach = [([False] * n) for r in range(m)]
        a_reach = [([False] * n) for r in range(m)]

        q = Queue()

        r = 0
        for c in range(n):
            q.put((r,c))
        c = 0
        for r in range(1, m):
            q.put((r,c))

        while not q.empty():
            r, c = q.get()
            h = heights[r][c]
            p_reach[r][c] = True

            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                # print(f"{nr=}, {nc=}")
                if (not p_reach[nr][nc]) and heights[nr][nc] >= h:
                    q.put((nr, nc))
        

        r = m-1
        for c in range(n):
            q.put((r,c))
        c = n-1
        for r in range(m-1):
            q.put((r,c))
        ret = []
        while not q.empty():
            r, c = q.get()
            h = heights[r][c]
            a_reach[r][c] = True

            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= m or nc< 0 or nc >= n:
                    continue
                if (not a_reach[nr][nc]) and heights[nr][nc] >= h:
                    q.put((nr, nc))
        
        for r in range(m):
            for c in range(n):
                if a_reach[r][c] and p_reach[r][c]:
                    ret.append([r, c])
        
        return ret
        