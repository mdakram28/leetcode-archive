class Solution:
    def numSquares(self, n: int) -> int:
        max_i = math.floor(math.sqrt(n))

        dp = [n] * (n+1)
        dp[0] = 0
        
        for target in range(1, n+1):
            for i in range(1, target+1):
                sq = i*i
                if sq > target:
                    break
                dp[target] = min(
                    dp[target],
                    dp[target-sq]+1
                )

        return dp[-1]





