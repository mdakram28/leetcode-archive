class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9+7
        
        @cache
        def count(rem, prev):
            if rem == 0: return 1
            
            ans = 0
            
            mask = 1
            for i in range(n):
                if rem & mask and (nums[i]%prev == 0 or prev%nums[i]==0):
                    ans = (ans + count(rem&(~mask), nums[i]))%mod
                mask <<= 1
                
            return ans
        
        all_set = int("1"*n, 2)
        
        return count(all_set, 1)