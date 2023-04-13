class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)
        while (r-l) > 1:
            mid = (l+r)//2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        if l >= len(nums) or nums[l] != target:
            return -1, -1
        last = l

        l = 0
        r = last
        while l<r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
        
        return l, last