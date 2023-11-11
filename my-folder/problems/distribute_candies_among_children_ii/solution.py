class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        dp = [0]*(n+1)
        dp[0] = 1
        dp_next = [0]*(n+1)
        
        for _ in range(3):
            # print(dp)
            total = 0
            for c in range(n+1):
                total += dp[c]
                if c >limit:
                    total -= dp[c-limit-1]
                dp_next[c] = total
            dp, dp_next = dp_next, dp
        
        # print(dp)
        return dp[-1]