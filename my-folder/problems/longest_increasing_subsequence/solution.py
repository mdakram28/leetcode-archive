class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            ind = bisect_left(nums, num, hi=ans)
            nums[ind] = num
            ans = max(ans, ind+1)
        
        return ans