class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        ns = len(strs[0])
        graph = [[] for i in range(n)]

        for i, s1 in enumerate(strs):
            for j, s2 in enumerate(strs):
                count = 0
                for c1, c2 in zip(s1, s2):
                    if c1 != c2:
                        count += 1
                    if count > 2:
                        break
                else:
                    graph[i].append(j)
        
        comp = 0
        visited = [False] * n
        def dfs(at):
            if visited[at]:
                return
            visited[at] = True
            for to in graph[at]:
                dfs(to)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                comp += 1
        
        return comp
