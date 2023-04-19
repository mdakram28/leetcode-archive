class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: return 0
        INF = float('inf')
        a,b,c,d = INF, INF, INF, INF
        w,x,y,z = -INF, -INF, -INF, -INF

        for num in nums:
            if num < a:
                a,b,c,d = num, a, b, c
            elif num < b:
                b,c,d = num, b, c
            elif num < c:
                c,d = num,c
            elif num < d:
                d = num
            
            if num > w:
                w,x,y,z = num, w, x, y
            elif num > x:
                x,y,z = num, x, y
            elif num > y:
                y,z = num, y
            elif num > z:
                z = num
        
        
        return min(
            z-a, y-b, x-c, w-d
        )