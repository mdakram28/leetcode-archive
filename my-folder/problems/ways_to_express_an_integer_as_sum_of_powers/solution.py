class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        
        @cache
        def numways(i, t):
            if t == 0: return 1
            if t-i**x < 0: return 0
            
            return (numways(i+1, t) + numways(i+1, t-i**x))%(10**9 + 7)
        
        return numways(1, n)