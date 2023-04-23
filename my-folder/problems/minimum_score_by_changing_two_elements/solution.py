class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        INF = float('inf')
        x, y, z = INF, INF, INF
        a, b, c = -INF, -INF, -INF
        for n in nums:
            if n < x:
                x, y, z = n, x, y
            elif n < y:
                y, z = n, y
            elif n < z:
                z = n
            
            if n > a:
                a, b, c = n, a, b
            elif n > b:
                b, c = n, b
            elif n > c:
                c = n
        # print(x, y, z, a)
        
        return min(a-z, b-y, c-x)