class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        visited = [False] * n
        graph = [[] for _ in range(n)]
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        for e in graph:
            e.sort(key=lambda to: vals[to], reverse=True)
            
        ans = -float('inf')
        
        def dfs(at, p):
            nonlocal ans
            if visited[at]: return
            visited[at] = True
            
            star_val = vals[at]
            for to in graph[at][:k]:
                if vals[to] <= 0: break
                star_val += vals[to]
            ans = max(ans, star_val)
            
            for to in graph[at]:
                if to == p: continue
                dfs(to, at)
                
                
        for i in range(n):
            if not visited[i]:
                dfs(i, None)
                
        return ans