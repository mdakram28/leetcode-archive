class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        g = defaultdict(dict)
        dest = max(max(e[0], e[1]) for e in edges)
        
        for a, b, t in edges:
            g[a][b] = min(g[a].get(b, t), t)
            g[b][a] = min(g[b].get(a, t), t)
        
        mintime = defaultdict(lambda: float('inf'))
        mintime[0] = passingFees[0]

        # (cost, time, node)
        q = [(passingFees[0], 0, 0)]

        while q:
            c, t, at = heappop(q)
            if at == dest: return c
            for to, td in g[at].items():
                t2 = t+td
                c2 = c+passingFees[to]
                if t2 > maxTime: continue
                
                if t2 >= mintime[to]: continue
                mintime[to] = t2
                heappush(q, (c2, t2, to))
                
                # if to == dest: continue
        return -1
        # ans = mincost[dest]
        # return ans if ans != float('inf') else -1
