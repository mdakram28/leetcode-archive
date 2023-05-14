class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        g = [[] for _ in range(n)]
        
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        found = []
        def dfs(at):
            found.append(at)
            visited[at] = True
            for to in g[at]:
                if not visited[to]:
                    dfs(to)
        
        ans = 0
        for at in range(n):
            if not visited[at]:
                found.clear()
                dfs(at)
                edges = sum(len(g[n]) for n in found)
                # print(found, edges)
                if edges == len(found)*(len(found)-1):
                    ans += 1
        
        return ans