class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        first = nums.index(1)
        last = nums.index(len(nums))
        if first < last:
            return first + len(nums)-last-1
        else:
            return first + len(nums)-last-1 -1