class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        total = 0
        ans = float('inf')

        for start in range(n):
            while total < target and end < n:
                total += nums[end]
                end += 1
            
            if total >= target:
                ans = min(ans, end-start)
            
            total -= nums[start]
        
        return 0 if ans == float('inf') else ans