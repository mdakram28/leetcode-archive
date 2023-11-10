class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n

        for r in range(1, m):
            dp = accumulate(dp)
        
        val = None
        for n in dp:
            val = n
        return val