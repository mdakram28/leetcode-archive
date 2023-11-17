class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1