class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l<r:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid+1
            else:
                r = mid
        return l if l < len(nums) and nums[l] == target else -1