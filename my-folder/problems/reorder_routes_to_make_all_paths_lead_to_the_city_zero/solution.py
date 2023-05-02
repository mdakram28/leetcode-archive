class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append((b, True))
            graph[b].append((a, False))
        
        ans = 0
        def dfs(at, p):
            nonlocal ans
            for to, fwd in graph[at]:
                if to == p:
                    continue
                if fwd:
                    ans += 1
                dfs(to, at)
        
        dfs(0, None)
        return ans