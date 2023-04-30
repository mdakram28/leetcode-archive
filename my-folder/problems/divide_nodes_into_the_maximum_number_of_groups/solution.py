class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        
        for a, b in edges:
            a -= 1
            b -= 1
            graph[a].append(b)
            graph[b].append(a)
            
        color = [0] * n
        def has_odd_cycle(at, c):
            if color[at]:
                return color[at] != c
            color[at] = c
            c = 1 if c == 2 else 2
            return any(has_odd_cycle(to, c) for to in graph[at])
        
        for at in range(n):
            if color[at] == 0 and has_odd_cycle(at, 1):
                return -1
        
        visited = [False] * n
        
        
        def check_all(at):
            if visited[at]: return 0
            visited[at] = True
            # print(f"Visiting {at}")
            
            ans = get_layers(at)
            
            for to in graph[at]:
                # check_all(to)
                ans = max(ans, check_all(to))
            return ans
            
        
        def get_layers(node):
            visited2 = {node: True}
            q = Deque([node])
            l = 0
            while q:
                l += 1
                for _ in range(len(q)):
                    at = q.popleft()
                    for to in graph[at]:
                        if to in visited2: continue
                        visited2[to] = True
                        q.append(to)
            # print(f"get_layers {node=}, {l=}")
            return l
        
        ans = 0
        for at in range(n):
            if not visited[at]:
                # print(f"Checking from {at}")
                ans += check_all(at)
        
        return ans
            
            
            