class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        nums.sort()
        
        @cache
        def can_make(i, t, l):
            # print(f"{i=}, {t=}, {n=}")
            if l==0: return t == 0
            if t < 0 or i == n: return False
            return can_make(i+1, t, l) or can_make(i+1, t-nums[i], l-1) 
            
        n = len(nums)
        total = sum(nums)
        for l in range(1, n-1):
            if (total*l)%n != 0: continue
            target = (total*l)//n
            # print(l, target)
            if can_make(0, target, l):
                return True
        return False
            