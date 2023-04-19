class Solution:
    def minimumSize(self, nums: List[int], op: int) -> int:
        nums.sort(reverse=True)
        lo = 1
        hi = nums[0]

        while lo < hi:
            mid = (lo+hi)//2
            # print(f"target = {mid}")

            req = sum((num-1)//mid for num in nums)
            
            # print(f"Required operations = {req}")
            
            if req > op:
                lo = mid+1
            else:
                hi = mid
        
        return lo
