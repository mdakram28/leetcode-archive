class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        while r-l>1:
            mid = (l+r)//2
            if nums[mid-1] != nums[mid] != nums[(mid+1)%len(nums)]:
                return nums[mid]
            elif nums[mid] == nums[mid-1]:
                if mid%2 == 0:
                    r = mid
                else:
                    l = mid+1
            else:
                if mid%2 == 0:
                    l = mid+1
                else:
                    r = mid
        
        return nums[l]
