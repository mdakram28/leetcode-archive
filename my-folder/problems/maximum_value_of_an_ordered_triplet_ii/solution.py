class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        t1 = []
        maxval = -float('inf')
        for num in nums:
            t1.append(maxval - num)
            maxval = max(maxval, num)
        
        ret = 0
        maxt1 = -float('inf')
        mint1 = float('inf')
        for num, t1 in zip(nums, t1):
            if num > 0:
                val = maxt1 * num
            elif num < 0:
                val = mint1 * num
            else:
                val = 0
            ret = max(ret, val)
            maxt1 = max(maxt1, t1)
            mint1 = min(mint1, t1)
        
        return ret