MAXN = 10**5+5
pf = list(range(MAXN + 1))

def sieve():
    p = 2
    while p * p <= MAXN:
        if pf[p] == p:
            for i in range(p * p, MAXN + 1, p):
                pf[i] = p
        p += 1
    return pf

@cache
def fact(n):
    ans = set()
    while n>1:
        f = pf[n]
        ans.add(f)
        while n%f == 0:
            n //= f
    return ans

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
    
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        global MAXN
        n = len(nums)
        MAXN = max(nums)+2

        pf = sieve()
        g = defaultdict(set)

        for num in nums:
            if num == 1: return len(nums) == 1
            factors = fact(num)
            for f in factors:
                g[f].update(factors)
        
        seen = set()

        def dfs(at):
            if at in seen: return
            seen.add(at)
            for to in g[at]:
                dfs(to)
        
        dfs(pf[nums[0]])
        return len(g) == len(seen)
        
        