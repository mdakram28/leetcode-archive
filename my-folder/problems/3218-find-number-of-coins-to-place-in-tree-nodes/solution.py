class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(edges)+1
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        coins = [0]*n
        
        def dfs(at, p):
            maxvals = [(-cost[at], at)]
            minvals = [(cost[at], at)]
            
            for to in g[at]:
                if to == p:
                    continue
                mx, mn = dfs(to, at)
                for val, node in mx:
                    heappush(maxvals, (val, node))
                    if len(maxvals) > 3:
                        heappop(maxvals)
                
                for val, node in mn:
                    heappush(minvals, (val, node))
                    if len(minvals) > 3:
                        heappop(minvals)
            
            vals = {}
            for val, node in maxvals:
                vals[node] = -val
            
            for val, node in minvals:
                vals[node] = val
                
            
            coins[at] = max(
                0,
                max(a*b*c for a, b, c in combinations(vals.values(), 3))
            )  if len(vals) >= 3 else 1
            
            return maxvals, minvals
                
        
        dfs(0, None)
        return coins
