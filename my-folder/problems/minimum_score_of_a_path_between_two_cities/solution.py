class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        
        for i, j, d in roads:
            i -= 1
            j -= 1
            graph[i].append((j, d))
            graph[j].append((i, d))
        
        visited = [False] * n
        ans = float('inf')
        def dfs(at):
            nonlocal ans
            
            if visited[at]: return
            visited[at] = True
            
            for to, d in graph[at]:
                ans = min(ans, d)
                dfs(to)
            
        dfs(0)
        return ans
            