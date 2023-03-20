class Solution:
    def isHappy(self, n: int) -> bool:
        found = set()
        while n != 1:
            # print(n)
            d = n
            n = 0
            while d > 0:
                n += (d%10) * (d%10)
                d //= 10
            
            if n in found:
                return False
            found.add(n)
        
        return True