class Solution:
    def numDecodings(self, s: str) -> int:
        DP = [0] * (len(s) + 1)
        DP[0] = 1
        for i in range(1, len(s) + 1):
            DP[i] = DP[i-1] if s[i-1] != '0' else 0
            if i > 1 and s[i-2] != '0':
                if s[i-1] <= '6':
                    if s[i-2] <= '2':
                        DP[i] += DP[i-2]
                elif s[i-2] <= '1':
                    DP[i] += DP[i-2]
        
        return DP[-1]