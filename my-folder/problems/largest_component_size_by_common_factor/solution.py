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
    while n>1:
        f = pf[n]
        yield f
        while n%f == 0:
            n //= f

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)

        MAXN = 10**5+5
        pf = sieve(MAXN)

        def lcm(a, b):
            return (a*b)//math.gcd(a, b)

        uf = UnionFind(MAXN)
        
        for num in nums:
            for f in fact(num, pf):
                uf.merge(num, f)

        f = defaultdict(int)
        for num in nums:
            f[uf.get_rep(num)] += 1 
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