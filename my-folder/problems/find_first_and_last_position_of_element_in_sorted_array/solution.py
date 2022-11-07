class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        if len(nums) > 0 and nums[0] == target:
            first = 0
        else:
            l = 0
            r = len(nums)-1
            while r-l>1:
                mid = (l+r)//2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid
            # print(f"first = {r}")
            if r >= 0 and r < len(nums) and nums[r] == target:
                first = r
        
        if first != -1:
            l = first
            r = len(nums)
            while r-l>1:
                mid = (l+r)//2
                # print(f"l={l}, r={r}, mid={mid}")
                if nums[mid] <= target:
                    l = mid
                else:
                    r = mid
            last = l
            return [first, last]
        else:
            return [-1, -1]
            
        