class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        '''
        isInfected[r][c]:
            0 : Uninfected
            1 : Infected
            2 : Infected & restricted
        '''
        m = len(isInfected)
        n = len(isInfected[0])

        borders = 0
        threatened = 0
        def dfs(r, c, id):
            nonlocal borders, threatened
            if r < 0 or r>=m or c < 0 or c>=n:
                return

            if isInfected[r][c] == 1:
                if visited[r][c] == 0:
                    visited[r][c] = 1
                    dfs(r-1, c, id)
                    dfs(r+1, c, id)
                    dfs(r, c-1, id)
                    dfs(r, c+1, id)
                else:
                    pass
            elif isInfected[r][c] == 0:
                if visited[r][c] == id:
                    borders += 1
                else:
                    borders += 1
                    threatened += 1
                    visited[r][c] = id
        
        def flood(r, c, find, repl):
            if r < 0 or r>=m or c < 0 or c>=n or isInfected[r][c] != find:
                return
            isInfected[r][c] = repl
            flood(r-1, c, find, repl)
            flood(r+1, c, find, repl)
            flood(r, c-1, find, repl)
            flood(r, c+1, find, repl)
        
        def expand(r, c, id):
            if r < 0 or r>=m or c < 0 or c>=n or visited[r][c] == 1:
                return
            visited[r][c] = 1
            if isInfected[r][c] == 0:
                isInfected[r][c] = 1
            elif isInfected[r][c] == 1:
                expand(r+1, c, id)
                expand(r-1, c, id)
                expand(r, c-1, id)
                expand(r, c+1, id)   

        total_walls = 0

        while True:
            # Day ---------------------------------------------------
            max_th = 0
            max_th_loc = (None, None)
            max_th_border = 0
            id = 3
            visited = [[0] * n for _ in range(m)]

            for r in range(m):
                for c in range(n):
                    if isInfected[r][c]==1 and visited[r][c] == 0:
                        
                        borders = 0
                        threatened = 0
                        dfs(r, c, id)
                        id += 1
                        if threatened > max_th:
                            max_th = threatened
                            max_th_loc = r, c
                            max_th_border = borders
            
            if max_th == 0:
                break
            total_walls += max_th_border
            # Restrict bordered region by making them dormant
            flood(*max_th_loc, 1, 2)

            # Night -------------------------------------------------

            visited = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if isInfected[r][c]==1 and visited[r][c] == 0:
                        expand(r, c, id)
                        id += 1

        return total_walls





