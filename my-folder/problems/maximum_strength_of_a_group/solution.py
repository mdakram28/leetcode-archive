class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def f(i, prev, taken):
            if i == n-1:
                if taken:
                    return max(prev, prev*nums[n-1])
                else:
                    return nums[n-1]
            
            return max(f(i+1, nums[i]*prev, True), f(i+1, prev, taken))
        
        return f(0, 1, False)