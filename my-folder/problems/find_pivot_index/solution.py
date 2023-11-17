class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        for i, num in enumerate(nums):
            right -= num
            if left == right: return i
            left += num
        return -1