class Solution:
    def findScore(self, nums: List[int]) -> int:
        ans = 0
        for i in sorted(range(len(nums)), key=lambda i: nums[i]):
            if nums[i] == 0: continue
            ans += nums[i]
            if i > 0:
                nums[i-1] = 0
            if i+1 < len(nums):
                nums[i+1] = 0
        
        return ans
