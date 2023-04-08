class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        inf = float('inf')
        
        q = deque()

        for r  in range(n):
            for c in range(n):
                if grid[r][c]==1:
                    for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                        nr, nc = r+dr, c+dc
                        if nr>=0 and nr<n and nc>=0 and nc<n and grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                        
        # print('\n'.join(map(str, grid)))
        # print('-----------------')

        for r in range(n):
            for c in range(n):
                grid[r][c] = grid[r][c]-1 if grid[r][c]>=1 else inf
        # print('\n'.join(map(str, grid)))
        # print('-----------------')

        while q:
            r,c = q.popleft()
            # print(r, c, )
            nd = grid[r][c]+1
            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr, nc = r+dr, c+dc
                if nr>=0 and nr<n and nc>=0 and nc<n and grid[nr][nc] > nd:
                    grid[nr][nc] = nd
                    q.append((nr, nc))
        # print('\n'.join(map(str, grid)))
        ret = max(map(max, grid))
        return ret if ret!= inf and ret!=0 else -1
            