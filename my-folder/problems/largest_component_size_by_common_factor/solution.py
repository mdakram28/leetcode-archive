def sieve(n):
    pf = list(range(n + 1))

    p = 2
    while p * p <= n:
        if pf[p] == p:
            for i in range(p * p, n + 1, p):
                pf[i] = p
        p += 1

    return pf

def fact(n, pf):
    ans = set()
    while n>1:
        f = pf[n]
        ans.add(f)
        while n%f == 0:
            n //= f
    return ans

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)

        MAXN = max(nums)+2
        pf = sieve(MAXN)

        def lcm(a, b):
            return (a*b)//math.gcd(a, b)

        # uf = UnionFind(MAXN)
        g = defaultdict(set)
        
        for num in nums:
            factors = fact(num, pf)
            for f in factors:
                g[f].update(factors)

        # print({k:v for k, v in g.items()})

        visited = defaultdict(int)
        def dfs(at, i):
            if visited[at]: return
            visited[at] = i
            for to in g[at]:
                dfs(to, i)
        
        # ans = 0
        for at in g.keys():
            # prev_l = len(seen)
            dfs(at, at)
            # ans = max(ans, len(seen)-prev_l)

        f = defaultdict(int)
        for num in nums:
            f[visited[pf[num]]] += 1

        return max(f.values())

class UnionFind:
    def __init__(self, n):
        self.rep = [i for i in range(n)]
    
    def get_rep(self, i):
        at = i
        r = self.rep[at]
        while r!=at:
            at, r = r, self.rep[r]

        at = i
        while at != r:
            at, self.rep[at] = self.rep[at], r
        
        return r
    
    def merge(self, a, b):
        r1, r2 = self.get_rep(a), self.get_rep(b)
        self.rep[r2] = r1

    def max_group_size(self):
        c = Counter(map(self.get_rep, self.rep))
        return c.most_common(1)[0][1]