class Solution:
    def partitionString(self, s: str) -> int:
        
        dp = [float('inf')] * (len(s)+1)
        dp[-1] = 0

        for r in range(len(s)):
            found = set()
            for l in range(r, -1, -1):
                if s[l] in found: break
                dp[r] = min(dp[r], 1+dp[l-1])
                found.add(s[l])

        return dp[-2]