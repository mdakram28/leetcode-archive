class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        minVal = min(nums)
        for num in nums:
            if num%minVal != 0: return 1
        
        return ceil(sum(1 for num in nums if num == minVal)/2)