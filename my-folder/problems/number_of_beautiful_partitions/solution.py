class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        mod = 10**9 + 7
        primes = ("2", "3", "5", "7")
        
        if s[0] not in primes or s[-1] in primes: return 0
        
        can_break = [i>0 and s[i] in primes and s[i-1] not in primes for i in range(n)]
        
        dp_prev = [1] * (n)
        dp = [0] * n
        
        
        for p in range(1, k):
            if p == 2:
                for r in range(minLength):
                    dp[r] = 0
            for r in range(minLength, n):
                if can_break[r]:
                    dp[r] = (dp[r-1] + dp_prev[r-minLength])%mod
                else:
                    dp[r] = dp[r-1]
            # print(dp)
            dp, dp_prev = dp_prev, dp 
        
        return dp_prev[-minLength]