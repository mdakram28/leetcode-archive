class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        inc_pref = 1
        n = len(nums)
        while inc_pref < n and nums[inc_pref] > nums[inc_pref-1]:
            inc_pref += 1
        
        inc_suff = n-1
        while inc_suff > 0 and nums[inc_suff-1] < nums[inc_suff]:
            inc_suff -= 1
        
        count = 0
        for i in range(max(0, inc_suff-1), n):
            next_start = nums[i+1] if i < (n-1) else float('inf')
            j = bisect_left(nums, next_start, hi=inc_pref)
            if j == i+1:
                j -= 1
            # print(i, next_start, j)
            count += j+1
        
        return count
