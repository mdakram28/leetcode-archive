class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while (end-start)>1 and nums[end] < nums[start]:
            # print(f"{start=}, {end=}")

            mid = (start+end)//2
            if nums[mid] < nums[start]:
                end = mid
            else:
                start = mid
        
        offset = end if nums[end] < nums[start] else start
        # print(f"{offset=}")

        idx = lambda i: (i+offset)%len(nums)

        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            mid_val = nums[idx(mid)]
            # print(f"{l=}, {r=}, {mid_val=}")
            if mid_val < target:
                l = mid+1
            elif mid_val >= target:
                r = mid
        
        if nums[idx(l)] == target:
            return idx(l)
        else:
            return -1
        

