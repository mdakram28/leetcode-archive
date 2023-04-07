class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visited = [[False]*n for r in range(n)]
        borders = [[0]*n for r in range(n)]

        def clear_visited(r, c):
            if r<0 or r>=n or c<0 or c>=n or not visited[r][c]:
                return
            visited[r][c] = False
            clear_visited(r-1, c)
            clear_visited(r+1, c)
            clear_visited(r, c-1)
            clear_visited(r, c+1)

        def flood(r, c):
            if r<0 or r>=n or c<0 or c>=n or grid[r][c]==0:
                return
            grid[r][c] = 0
            flood(r-1, c)
            flood(r+1, c)
            flood(r, c-1)
            flood(r, c+1)

        def get_size(r, c):
            if r<0 or r>=n or c<0 or c>=n or grid[r][c] == 0 or visited[r][c]:
                return 0
            visited[r][c] = True
            total = 1
            total += get_size(r-1, c)
            total += get_size(r+1, c)
            total += get_size(r, c-1)
            total += get_size(r, c+1)
            return total
        
        def extend_border(r, c, val):
            if r<0 or r>=n or c<0 or c>=n or visited[r][c]:
                return
            elif grid[r][c]==0:
                visited[r][c] = True
                borders[r][c] += val
                return
            
            visited[r][c] = True
            extend_border(r-1, c, val)
            extend_border(r+1, c, val)
            extend_border(r, c-1, val)
            extend_border(r, c+1, val)

        max_size = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    size = get_size(r, c)
                    max_size = max(max_size, size)
                    clear_visited(r, c)
                    extend_border(r, c, size)
                    clear_visited(r, c)
                    flood(r, c)

        print(borders)
        return max(max_size, max(map(max, borders))+1)