class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = 0
        while n > 1:
            total += n//2
            if n%2 == 0:
                n //= 2
            else:
                n = ceil(n/2)
        
        return total
