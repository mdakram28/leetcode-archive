class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp = [0]*(n+1)
        d = defaultdict(list)
        
        for off in offers:
            d[off[1]].append(off)
        
        # ans = 0
        for h in range(n):
            dp[h] = dp[h-1]
            for off in d[h]:
                dp[h] = max(dp[h], off[2]+dp[off[0]-1])
        # print(dp)
        return dp[n-1]
            