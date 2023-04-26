class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign = 1
        total = 0
        i = 0
        while n:
            i += 1
            total += sign*(n%10)
            n //= 10
            sign = -sign
        
        return total if i%2 else -total