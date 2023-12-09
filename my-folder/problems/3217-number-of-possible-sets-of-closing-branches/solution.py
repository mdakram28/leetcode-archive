class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b, d in roads:
            g[a].append((b, d))
            g[b].append((a, d))
        
        def withinMaxDist(avail):
            for start in range(n):
                if not avail[start]: continue
                    
                dist = [float('inf')]*n
                dist[start] = 0
                q = [(0, start)]
                while q:
                    d, at = heappop(q)
                    for to, d2 in g[at]:
                        if avail[to] and d+d2 < dist[to]:
                            dist[to] = d+d2
                            heappush(q, (d+d2, to))
                
                for at in range(n):
                    if avail[at] and dist[at] > maxDistance:
                        return False
                # print(start, dist)
            
            return True
        
        ans = 0
        for i in range(2**n):
            nodes = [((i>>node)&1) == 1 for node in range(n)]
            # print([at for at in range(n) if nodes[at]])
            if withinMaxDist(nodes):
                ans += 1
        
        return ans
        
