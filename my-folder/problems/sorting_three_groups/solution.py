class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        @cache
        def f(i, maxg):
            if i < 0: return 0
            ans = float('inf')
            for g in range(1, maxg+1):
                ans = min(ans, f(i-1, g) + (1 if g != nums[i] else 0))
            return ans
        
        n = len(nums)
        ans = min(f(n-1, 1), f(n-1, 2), f(n-1, 3))
        return ans