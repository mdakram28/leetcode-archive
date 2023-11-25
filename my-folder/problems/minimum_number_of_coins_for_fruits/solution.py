class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        dp = [0]*(n+1)
        # dp[-1] = 0
        
        for i in range(n-1, -1, -1):
            dp[i] = prices[i]+dp[i+1]
            for j in range(i+2, min(i+i+3, n+1)):
                # print(i, j)
                dp[i] = min(dp[i], prices[i] + dp[j])
        # print(dp)
        return dp[0]