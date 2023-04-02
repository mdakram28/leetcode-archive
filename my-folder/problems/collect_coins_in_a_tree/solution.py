class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(edges)+1
        g = [set() for _ in range(n)]
        for n1, n2 in edges:
            g[n1].add(n2)
            g[n2].add(n1)
        
        to_remove = set()
        for node in range(n):
            if len(g[node]) == 1 and coins[node] == 0:
                to_remove.add(node)
        
        next_rem = set()
        while to_remove:
            next_rem.clear()
            for rem in to_remove:
                if len(g[rem]) == 0:
                    return 0
                p = next(iter(g[rem]))
                g[p].remove(rem)
                g[rem].clear()
                if len(g[p]) == 1 and coins[p] == 0:
                    next_rem.add(p)
            to_remove, next_rem = next_rem, to_remove
        
        to_remove.clear()
        next_rem.clear()
        for node in range(n):
            if coins[node] == 1 and len(g[node]) == 1:
                to_remove.add(node)
        
        for rem in to_remove:
            if len(g[rem]) == 0:
                return 0
            p = next(iter(g[rem]))
            g[p].remove(rem)
            g[rem].clear()
            if len(g[p]) == 1:
                next_rem.add(p)
        to_remove, next_rem = next_rem, to_remove
        
        for rem in to_remove:
            if len(g[rem]) == 0:
                return 0
            p = next(iter(g[rem]))
            g[p].remove(rem)
            g[rem].clear()
        
        print(g)
        
        return sum(len(s) for s in g)
            
            