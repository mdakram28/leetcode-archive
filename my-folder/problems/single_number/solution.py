class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = 0
        for num in nums:
            t = t ^ num
        return t