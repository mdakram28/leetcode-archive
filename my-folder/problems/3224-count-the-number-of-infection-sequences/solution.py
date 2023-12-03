
class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        mod = 10**9+7
        fact = [1]*(n+1)
        for i in range(2, n+1):
            fact[i] = (i * fact[i-1])%mod
        # @cache
        # def fact(n):
        #     if n <= 1:
        #         return 1
        #     return n*fact(n-1)
        
        # def ncr(n, r):
        #     num = den = 1
        #     for i in range(r):
        #         num = (num * (n - i)) % mod
        #         den = (den * (i + 1)) % mod
        #     return (num * pow(den, mod - 2, mod)) % mod
        
        num = 1
        den = 1
        c = 0
        
        for l, r in pairwise(sick):
            x = r-l-1
            if x >= 1:
                total = pow(2, x-1, mod)
                # ans = (ans*ncr(c+x, c)*total)%mod
                num = (num*fact[c+x]*total)%mod
                den = (den*fact[c]*fact[x])%mod
                c += x
        
        
        x = sick[0]
        if x >= 1:
            total = 1
            # ans = (ans*ncr(c+x, c)*total)%mod
            num = (num*fact[c+x]*total)%mod
            den = (den*fact[c]*fact[x])%mod
            c += x
        
        x = n-1-sick[-1]
        if x >= 1:
            total = 1
            # ans = (ans*ncr(c+x, c)*total)%mod
            num = (num*fact[c+x]*total)%mod
            den = (den*fact[c]*fact[x])%mod
            c += x
        
        ans = (num * pow(den, mod - 2, mod)) % mod
        return ans
            
