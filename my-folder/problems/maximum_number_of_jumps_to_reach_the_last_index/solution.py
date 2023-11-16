class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        @cache
        def max_jumps(i):
            if i == len(nums)-1: return 0
            ans = -float('inf')
            for j in range(i+1, len(nums)):
                if abs(nums[j]-nums[i]) <= target:
                    ans = max(ans, max_jumps(j)+1)
            return ans
        
        ans = max_jumps(0)
        return -1 if ans == -float('inf') else ans