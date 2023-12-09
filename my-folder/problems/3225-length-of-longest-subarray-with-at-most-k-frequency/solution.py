class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        f = defaultdict(int)
        
        n = len(nums)
        l = 0
        ans = 0
        
        for r in range(len(nums)):
            f[nums[r]] += 1
            
            while l<r and f[nums[r]] > k:
                f[nums[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans
