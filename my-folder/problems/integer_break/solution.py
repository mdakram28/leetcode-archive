class Solution:
    def integerBreak(self, n: int) -> int:

        @cache
        def maxProd(n):
            ret = n
            for i in range(1, n//2 + 1):
                ret = max(ret, maxProd(i)*maxProd(n-i))
            return ret
        
        ret = 0
        for i in range(1, n//2 + 1):
            ret = max(ret, maxProd(i)*maxProd(n-i))
        
        return ret
