class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float('inf')]*n
        dp.append(0)
        # for i in range(n):
        #     dp[i][i] = 1
        
        f = defaultdict(int)
        for r in range(n):
            f.clear()
            un = 0
            for l in range(r, -1, -1):
                if f[nums[l]] == 0:
                    un += 1
                elif f[nums[l]] == 1:
                    un -= 1
                f[nums[l]] += 1
                dp[r] = min(dp[r], dp[l-1] + k + r-l+1-un)
        
        # print(dp)
        return dp[-2]