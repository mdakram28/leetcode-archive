class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        @cache
        def max_score_subarray(l, r, lval, rval):
            if l == r:
                return lval * nums[l] * rval
            max_val = 0
            for i in range(l, r+1):
                max_val = max(
                    max_val, 
                    max_score_subarray(l, i-1, lval, nums[i]) +
                    max_score_subarray(i+1, r, nums[i], rval) +
                    nums[i]*lval*rval
                )
            return max_val
        
        return max_score_subarray(0, len(nums)-1, 1, 1)