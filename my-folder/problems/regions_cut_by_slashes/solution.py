class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        graph = [[] for _ in range(n*n*4)]

        def connect(n1, n2):
            graph[n1].append(n2)
            graph[n2].append(n1)

        for r in range(n):
            for c in range(n):
                node = (r*n+c)*4
                print(node)
                if grid[r][c] == '/':
                    connect(node+0, node+2)
                    connect(node+1, node+3)
                elif grid[r][c] == '\\':
                    connect(node+0, node+3)
                    connect(node+1, node+2)
                else:
                    connect(node+0, node+1)
                    connect(node+0, node+2)
                    connect(node+0, node+3)
        
        for r in range(n):
            for c in range(n):
                node = (r*n+c)*4
                if r>0:
                    up = ((r-1)*n+c)*4
                    connect(node+0, up+1)
                if c>0:
                    left = (r*n+(c-1))*4
                    connect(left+3, node+2)
                if r<(n-1):
                    down = ((r+1)*n+c)*4
                    connect(down+0, node+1)
                if c<(n-1):
                    right = (r*n+(c+1))*4
                    connect(right+2, node+3)
        
        visited = [False] * (n*n*4)
        def visit(at):
            if visited[at]:
                return
            visited[at] = True
            for to in graph[at]:
                visit(to)

        regions = 0
        for node in range(n*n*4):
            if not visited[node]:
                regions += 1
                visit(node)
        
        return regions


