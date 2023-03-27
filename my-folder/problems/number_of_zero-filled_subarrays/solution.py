class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ways = 0
        
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] != 0:
                i += 1 
                continue
            start = i
            while i < n and nums[i] == 0:
                i += 1
            num = i-start
            ways += (num*(num+1))//2
        
        return ways