class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads)+1
        g = [[] for _ in range(n)]
        
        for i, j in roads:
            g[i].append(j)
            g[j].append(i)
        
        ans = 0
        def dfs(at, p):
            nonlocal ans
            count = 1
            for to in g[at]:
                if to == p: continue
                t = dfs(to, at)
                ans += math.ceil(t/seats)
                count += t
            return count
        
        dfs(0, None)
        
        return ans
        
        
        