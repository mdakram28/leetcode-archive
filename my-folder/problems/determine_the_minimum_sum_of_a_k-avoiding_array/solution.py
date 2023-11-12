class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        def sigma(n):
            return (n*(n+1))//2
        def rangesum(l, r):
            if r < l or r<=0 or l<=0: return 0
            return sigma(r)-sigma(l-1)
        
        l = sigma(min(n, k//2))
        r = rangesum(k, n+(k-k//2-1))
        return l+r