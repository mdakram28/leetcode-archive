class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        lo = 0
        hi = max(nums)
        while lo < hi:
            mid = (lo+hi)//2
            
            taken = False
            count = 0
            for num in nums:
                if taken: 
                    taken = False
                    continue
                if num <= mid:
                    count += 1
                    taken = True
            
            if count < k:
                lo = mid+1
            else:
                hi = mid
        
        return lo
                    