from collections import defaultdict

class Solution:
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        neg_inf = float('-inf')
        pos_inf = float('inf')

        dp = [pos_inf] * (amount+1)
        dp[0] = 0

        for t in range(1, amount+1):
            count = pos_inf
            for c in coins:
                if c <= t:
                    # print(f"{t=}, {c=}")
                    count = min(count, dp[t-c] + 1)
            dp[t] = count
            # print(f"dp[{t}] = {dp[t]}")

        return -1 if dp[-1] == pos_inf else dp[-1]