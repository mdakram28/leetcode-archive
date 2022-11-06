class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums)-1
        i = 0
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return j+1