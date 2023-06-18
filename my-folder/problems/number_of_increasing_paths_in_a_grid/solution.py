class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10**9+7

        dp = [[None]*n for _ in range(m)]

        def count(r, c):
            if dp[r][c] is not None: return dp[r][c]
            ans = 1
            for dr,dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr, nc = r+dr, c+dc
                if nr >=0 and nr<m and nc>=0 and nc<n and grid[nr][nc] > grid[r][c]:
                    ans += count(nr, nc)
            dp[r][c] = ans
            return ans%mod
        
        ans = 0
        for r in range(m):
            for c in range(n):
                ans += count(r, c)
        
        return ans%mod