class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        count = 0
        ind = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                count += 1
                ind = i
        
        if count == 0:
            return 0
        if count > 1:
            return -1
        if nums[-1] > nums[0]:
            return -1
        
        return n-ind