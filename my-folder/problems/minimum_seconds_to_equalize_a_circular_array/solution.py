class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        maxd = {}
        previ = {}
        
        for i, num in enumerate(nums):
            previ[num] = i-len(nums)
            maxd[num] = 0
        
        for i, num in enumerate(nums):
            diff = math.ceil((i-previ[num]-1)/2)
            maxd[num] = max(maxd[num], diff)
            previ[num] = i
        return min(maxd.values())