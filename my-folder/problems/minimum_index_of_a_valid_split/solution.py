class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dom = nums[0]
        domc = 0
        for num in nums:
            if num == dom:
                domc += 1
            elif domc == 0:
                dom = num
                domc = 1
            else:
                domc -= 1 
        
        lc = 0
        rc = nums.count(dom)
        for split in range(len(nums)-1):
            if nums[split] == dom:
                lc += 1
                rc -= 1
            if lc*2 > split+1 and rc*2>len(nums)-split-1:
                return split
        return -1
        
        
        
        
        
        