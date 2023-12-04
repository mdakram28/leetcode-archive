class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        if n == 1: return 0

        nums.sort()
        def at_least_p_pairs(maxd):
            prevprev = 0
            prev = 1 if nums[1]-nums[0] <= maxd else 0
            for i in range(2, n):
                curr = prev
                if nums[i]-nums[i-1] <= maxd:
                    curr = max(prev, 1+prevprev)
                if curr >= p:
                    return True
                prevprev, prev = prev, curr
            return prev >= p
        
        lo = 0
        hi = nums[-1]-nums[0]
        # print(nums)
        while lo < hi:
            mid = lo + (hi-lo)//2
            if at_least_p_pairs(mid):
                # print(mid, "can_make")
                hi = mid
            else:
                # print(mid, "can_not")
                lo = mid+1

        return lo
