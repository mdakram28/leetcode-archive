class Solution:
    def findMin(self, nums: List[int]) -> int:
        t = nums[0]
        l = 0
        r = len(nums)

        while l < r:
            mid = (l+r)//2
            if nums[mid] < t:
                r = mid
            else:
                l = mid+1
        
        return nums[l%len(nums)]