class Solution:
    def rob(self, nums: List[int]) -> int:
        max_inc = nums[0]
        max_exc = 0

        for num in nums[1:]:
            max_inc, max_exc = (max_exc + num), max(max_inc, max_exc)
        
        return max(max_inc, max_exc)