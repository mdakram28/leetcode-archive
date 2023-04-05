class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        l = math.ceil(len(nums)/2)
        
        i = 0
        while l < len(nums):
            t = nums[i]*2
            r = len(nums)
            while l<r:
                mid = (l+r)//2
                if nums[mid] < t:
                    l = mid+1
                else:
                    r = mid
            if l < len(nums):
                l += 1
                i += 1
        
        return i*2