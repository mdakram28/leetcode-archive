class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        @cache
        def is_pal(l, r):
            if r <= l: return True
            return s[l] == s[r] and is_pal(l+1, r-1)
        
        dp = [0]
        for i in range(len(s)):
            count = 0
            for j in range(i-k+1, -1, -1):
                if s[i] == s[j] and is_pal(j+1, i-1):
                    count = dp[j] + 1
                    break
            
            dp.append(max(dp[-1], count))
            
        return dp[-1]