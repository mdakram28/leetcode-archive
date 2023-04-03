class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        pref = 0
        i = 0
        while i < len(nums):
            pref += nums[i]
            if pref <= 0:
                break
            i += 1
        
        return i