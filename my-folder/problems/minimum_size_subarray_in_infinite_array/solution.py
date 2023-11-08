class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        maxsum = sum(nums)
        extra = n * (target//maxsum)
        target = target%maxsum
        
        nums.append(0)
        t = 0
        ind = {}
        ind[0] = -1
        for i in range(n):
            nums[i] = nums[i-1] + nums[i]
            ind[nums[i]] = i
        
        
        minlen = float('inf')
        for i in range(n):
            if nums[i] >= target:
                rem = nums[i] - target
                if rem in ind:
                    minlen = min(minlen, i - ind[rem])
            else:
                rem = target - nums[i]
                if (maxsum - rem) in ind:
                    minlen = min(minlen, i+1 + n-ind[maxsum-rem]-1)
        
        return (minlen+extra) if minlen != float('inf') else -1