class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (high+1)
        dp[0] = 1
        
        for l in range(low):
            if l >= zero:
                dp[l] = (dp[l] + dp[l-zero]) % mod
            if l >= one:
                dp[l] = (dp[l] + dp[l-one]) % mod
        
        ans = 0
        for l in range(low, high+1):
            if l >= zero:
                dp[l] = (dp[l] + dp[l-zero]) % mod
            if l >= one:
                dp[l] = (dp[l] + dp[l-one]) % mod
            
            ans = (ans + dp[l]) % mod
        
        # print(dp)

        return ans