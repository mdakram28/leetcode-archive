class Solution:
    def countDigits(self, num: int) -> int:
        n = num
        total = 0
        while n:
            d = n%10
            if num%d == 0:
                total += 1
            n //= 10
        return total