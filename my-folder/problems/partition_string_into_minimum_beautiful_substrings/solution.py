class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        powers = set()
        for i in count(0):
            if 5**i > 1<<15: break
            powers.add(bin(5**i)[2:])
        
        # print(powers)
        dp = [float('inf')]*len(s) + [0]
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0': continue
            for j in range(i+1, len(s)+1):
                # print(i,j,s[i:j], s[i:j] in powers)
                if s[i:j] in powers:
                    dp[i] = min(dp[i], 1+dp[j])
        # print(dp)
        return dp[0] if dp[0] !=float('inf') else -1