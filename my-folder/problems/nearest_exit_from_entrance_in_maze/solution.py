class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        q = set()
        nextq = set()

        maze[entrance[0]][entrance[1]] = '+'
        r, c = entrance

        for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
            nr, nc = r+dr, c+dc
            if nr>=0 and nr<m and nc>=0 and nc<n and maze[nr][nc] != '+':
                q.add((nr ,nc))


        d = 1
        while q:
            nextq.clear()
            for r, c in q:
                if r == 0 or r == m-1 or c == 0 or c == n-1:
                    return d
                # print(r, c)
                if r > 0 and maze[r-1][c] == '.':
                    # if r == 1: return d
                    maze[r-1][c] = '+'
                    nextq.add((r-1, c))
                if r < m-1 and maze[r+1][c] == '.':
                    # if r== m-2: return d
                    maze[r+1][c] = '+'
                    nextq.add((r+1, c))
                if c > 0 and maze[r][c-1] == '.':
                    # if c == 1: return d
                    maze[r][c-1] = '+'
                    nextq.add((r, c-1))
                if c < n-1 and maze[r][c+1] == '.':
                    # if c == n-2: return d
                    maze[r][c+1] = '+'
                    nextq.add((r, c+1))
            q, nextq = nextq, q
            
            d += 1
        return -1
