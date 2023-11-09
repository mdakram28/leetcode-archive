def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prime[1] = False
    return prime

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        is_prime = sieve(n+5)
        
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        @cache
        def count_comp(at, p):
            if is_prime[at]:
                return 0
            return 1 + sum(count_comp(to, at) for to in g[at] if to != p)
        
        total = 0
        for at in range(1, n+1):
            if not is_prime[at]: continue
            T = 0
            for to in g[at]:
                comp = count_comp(to, None)
                T += comp
                total -= comp*comp
                # print(at, comp)
            total += T*T + 2*T
        
        return total // 2
                
            
            