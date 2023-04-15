class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edges = [[] for i in range(n)]
        for n1, n2 in connections:
            edges[n1].append(n2)
            edges[n2].append(n1)
        
        last_id = 0
        ids = [0] * n
        on_stack = [False] * n
        low = [0] * n
        stack = []
        # scc = 0
        crit = []

        def dfs(at, p):
            nonlocal last_id
            ids[at] = low[at] = last_id = last_id+1
            on_stack[at] = True
            stack.append(at)

            for to in edges[at]:
                if to == p: continue
                if not ids[to]:
                    dfs(to, at)
                if on_stack[to]: 
                    low[at] = min(low[at], low[to])
                  
            if low[at] == ids[at]:
                while (node := stack.pop()) != at:
                    on_stack[node] = False
                    # low[node] = ids[at]
                on_stack[at] = False
                if p!=-1:
                    crit.append((at, p))

        dfs(0, -1)
        return crit