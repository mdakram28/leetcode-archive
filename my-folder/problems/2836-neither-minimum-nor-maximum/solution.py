class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2: return -1
        a, b = min(nums), max(nums)
        return next(val for val in nums if val != a and val != b)
