class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cols = len(s) + 1
        rows = len(t) + 1
        dp_prev = [1] * cols
        dp = [0] * cols

        for r in range(1, rows):
            dp[0] = 0
            for c in range(1, cols):
                if s[c-1] == t[r-1]:
                    dp[c] = dp[c-1] + dp_prev[c-1]
                else:
                    dp[c] = dp[c-1]
            # print(dp)
            dp, dp_prev = dp_prev, dp

        return dp_prev[-1]