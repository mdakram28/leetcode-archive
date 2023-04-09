class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = Deque()
        inf = float('inf')

        lock_grid = [[0] * n for r in range(m)]
        key_grid = [[0] * n for r in range(m)]
        keys = []
        ALL_KEYS = 0
        start_pos = None
        

        for r in range(m):
            for c in range(n):
                if 'A' <= grid[r][c] <= 'Z':
                    lock_grid[r][c] = 1<<(ord(grid[r][c])-ord('A'))
                elif 'a' <= grid[r][c] <= 'z':
                    key_grid[r][c] = 1<<(ord(grid[r][c])-ord('a'))
                    keys.append((r, c))
                    ALL_KEYS |= key_grid[r][c]
                elif grid[r][c] == '@':
                    start_pos = (r, c)
        
        @cache
        def find_new_keys(r, c, keys_held):
            q.clear()
            q.append((0, r, c))
            dist = [[inf]*n for r in range(m)]
            dist[r][c] = 0
            while q:
                d, r, c = q.popleft()
                d += 1
                for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                    nr, nc = r+dr, c+dc
                    if nr<0 or nr>=m or nc<0 or nc>=n or grid[nr][nc] == '#':
                        continue
                    if lock_grid[nr][nc] == 0 or lock_grid[nr][nc]&keys_held:
                        # print(f"Can go {nr},{nc}")
                        if d < dist[nr][nc]:
                            dist[nr][nc] = d
                            q.append((d, nr, nc))
            # print(dist)
            ret = []
            for r,c in keys:
                if dist[r][c] != inf and key_grid[r][c]&keys_held == 0:
                    ret.append((dist[r][c], r, c))
            
            return ret

        def dfs(r,c, keys_held):
            if keys_held == ALL_KEYS:
                return 0
            min_dist = inf
            for dist, kr, kc in find_new_keys(r, c, keys_held):
                # print(f"From {r},{c}, key at {kr},{kc} {dist=}")
                min_dist = min(min_dist, dist + dfs(kr, kc, keys_held | key_grid[kr][kc]))
            return min_dist

        ret = dfs(start_pos[0], start_pos[1], 0)
        return ret if ret != inf else -1




