class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i0 = 0
        i1 = 0
        i2 = len(nums) - 1

        while i2 >= i1:
            # print(f"{nums=}, {i0=}, {i1=}, {i2=}")
            if nums[i1] == 2:
                nums[i1], nums[i2] = nums[i2], nums[i1]
                i2 -= 1
            elif nums[i1] == 1:
                i1 += 1
            else:
                nums[i1], nums[i0] = nums[i0], nums[i1]
                i1 += 1
                i0 += 1