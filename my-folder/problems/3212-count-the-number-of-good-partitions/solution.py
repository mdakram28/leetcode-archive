class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        
        lastind = {}
        for i, num in enumerate(nums):
            lastind[num] = i
        
        r = -1
        count = 0
        for i, num in enumerate(nums):
            r = max(r, lastind[num])
            if i == r:
                count += 1
                
        return pow(2, count-1, 10**9+7)
