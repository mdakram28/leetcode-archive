class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # ev = [(s, 1) s, e in nums] + [(e+1, -1) s, e in nums]
        # ev.sort()
        pres = set()
        for s, e in nums:
            for num in range(s, e+1):
                pres.add(num)
        return len(pres)
        # prev = 0
        # total = 0
        # for x, d in ev:
        #     total += d
        #     if total > 0:
                
            