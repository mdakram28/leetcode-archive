class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_p = nums[0]
        max_p = nums[0]
        ret = nums[0]
        for num in nums[1:]:
            choices = (num, num*min_p, num*max_p)
            min_p = min(choices)
            max_p = max(choices)
            ret = max(ret, max_p)
        return ret