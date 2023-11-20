class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def numWays(at, steps):
            if at < 0 or at >= arrLen: return 0
            if steps == 0: return 1 if at == 0 else 0

            return (numWays(at-1,steps-1) + numWays(at, steps-1) + numWays(at+1, steps-1))%(10**9+7)
        
        return numWays(0, steps)