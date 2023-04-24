class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q1 = Deque()
        q2 = Deque()
        v1 = [[False] * n for _ in range(n)]
        v2 = [[False] * n for _ in range(n)]

        def is_outside(r, c, q, v):
            if r<0 or r>=n or c<0 or c>=n or v[r][c]:
                return False

            if grid[r][c] == 0:
                return True
            else:
                v[r][c] = True
                ret = is_outside(r-1, c, q, v)
                ret = is_outside(r+1, c, q, v) or ret
                ret = is_outside(r, c-1, q, v) or ret
                ret = is_outside(r, c+1, q, v) or ret
                if ret:
                    q.append((r, c))
                return False


        for r in range(n):
            for c in range(n):
                if not v1[r][c] and grid[r][c] == 1:
                    if not q1:
                        is_outside(r, c, q1, v1)
                    else:
                        is_outside(r, c, q2, v2)
                        break
        d = 0
        while q1 and q2:


            d += 1
            for _ in range(len(q1)):
                r, c = q1.popleft()
                for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= n or nc < 0 or nc >= n or v1[nr][nc]:
                        continue
                    
                    if grid[nr][nc]:
                        return grid[nr][nc] + d - 1
                    else:
                        grid[nr][nc] = d
                        q1.append((nr, nc))
                        v1[nr][nc] = True
                        
            
            for _ in range(len(q2)):
                r, c = q2.popleft()
                for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= n or nc < 0 or nc >= n or v2[nr][nc]:
                        continue
                    
                    if grid[nr][nc]:
                        return grid[nr][nc] + d - 1
                    else:
                        grid[nr][nc] = d
                        q2.append((nr, nc))
                        v2[nr][nc] = True


        return -1