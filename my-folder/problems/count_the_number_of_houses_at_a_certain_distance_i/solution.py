class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        result = [0]*(n+1)
        
        g = defaultdict(set)
        for at in range(n):
            if at-1 >= 0:
                g[at].add(at-1)
            if at+1 < n:
                g[at].add(at+1)
        g[x-1].add(y-1)
        g[y-1].add(x-1)
        
        def add_all_dist(at):
            nonlocal result
            
            q = [(at, 0)]
            seen = {at}
            for at, d in q:
                result[d-1] += 1
                for to in g[at]:
                    if to not in seen:
                        q.append((to, d+1))
                        seen.add(to)
        
        
        for at in range(n):
            add_all_dist(at)
        
        return result[:-1]
        