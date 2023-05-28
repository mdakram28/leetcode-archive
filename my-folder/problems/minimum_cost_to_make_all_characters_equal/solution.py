class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        dp_fwd = [(0, 0)]*(n+1)
        
        for i in range(1, n+1):
            if s[i-1] == "1":
                dp_fwd[i] = (dp_fwd[i-1][0], i+dp_fwd[i-1][0])
            else:
                dp_fwd[i] = (i+dp_fwd[i-1][1], dp_fwd[i-1][1])
        
        dp_bwd = [(0, 0)]*(n+1)
        
        for i in range(1, n+1):
            if s[-i] == "1":
                dp_bwd[i] = (dp_bwd[i-1][0], i+dp_bwd[i-1][0])
            else:
                dp_bwd[i] = (i+dp_bwd[i-1][1], dp_bwd[i-1][1])
                
        ans = float('inf')
        for i in range(n):
            ans = min(ans, dp_fwd[i][0] + dp_bwd[n-i][0], dp_fwd[i][1] + dp_bwd[n-i][1])
        return ans