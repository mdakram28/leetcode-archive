class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    new_len = dp[j] + 1
                    if new_len > dp[i]:
                        dp[i] = new_len
                        count[i] = count[j]
                    elif new_len == dp[i]:
                        count[i] += count[j]
        max_len = max(dp)
        return sum(c for l, c in zip(dp, count) if l == max_len)