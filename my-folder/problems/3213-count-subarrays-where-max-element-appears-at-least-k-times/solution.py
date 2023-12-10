class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        val = max(nums)
        
        ind = {}
        count = 0
        ans = 0
        
        for i in range(n):
            if nums[i] != val:
                if count-k+1 in ind:
                    ans += ind[count-k+1] + 1
                continue
            count += 1
            ind[count] = i
            if count-k+1 in ind:
                ans += ind[count-k+1] + 1
        
        return ans
        
            
