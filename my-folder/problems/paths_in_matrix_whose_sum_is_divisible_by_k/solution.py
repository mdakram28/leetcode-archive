class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10**9+7
        
        dp = [[[None]*n for r in range(m)] for rem in range(k)]
        grid[-1][-1] %= k
        
        # @cache
        def num_rem(r, c, rem):
            if r >= m or c >= n: return 0
            if r == m-1 and c == n-1:
                return 1 if grid[-1][-1] == rem else 0
            
            if dp[rem][r][c] is not None:
                return dp[rem][r][c]
            
            new_rem = (rem - grid[r][c])%k
            ans = (num_rem(r+1, c, new_rem) + num_rem(r, c+1, new_rem))%mod
            dp[rem][r][c] = ans
            # print(f"{rem=}, {r=}, {c=} => {ans}")
            return ans
        
        ans = num_rem(0, 0, 0)
        # print('\n'.join(map(str, dp)))
        
        return ans
        