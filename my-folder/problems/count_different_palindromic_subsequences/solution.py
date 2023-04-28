class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        mod = 10**9+7
        dp = [[0]*n for l in range(n)]

        last_idx = {}

        prev_idx = [-1] * n
        for i in range(n):
            if s[i] in last_idx:
                prev_idx[i] = last_idx[s[i]]
            last_idx[s[i]] = i

        last_idx = {}
        next_idx = [n] * n
        for i in range(n-1, -1, -1):
            if s[i] in last_idx:
                next_idx[i] = last_idx[s[i]]
            last_idx[s[i]] = i

        for r in range(n):
            dp[r][r] = 1
            for l in range(r-1, -1, -1):
                if s[l] == s[r]:
                    nl, nr = next_idx[l], prev_idx[r]
                    dp[l][r] = (dp[l+1][r-1]*2 + (2 if nl>nr else 1 if nl==nr else -dp[nl+1][nr-1])) % mod
                else:
                    dp[l][r] = (dp[l+1][r] + dp[l][r-1] - dp[l+1][r-1]) % mod
        

        return dp[0][-1]