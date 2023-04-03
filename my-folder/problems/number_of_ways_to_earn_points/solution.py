class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (target+1)
        dp[0] = 1
        for count, marks in types:
            
            for t in range(target, 0, -1):
                used = 1
                rem = t-marks
                while rem >= 0 and used <= count:
                    dp[t] = (dp[t] + dp[rem]) % mod
                    rem -= marks
                    used += 1
        
        return dp[-1]