class Solution:
    def countDigitOne(self, n: int) -> int:
        total = 0

        d = 1
        while d <= n:
            digit = (n//d)%10
            left = n//(d*10)
            right = n%d
            if digit == 0:
                total += left * d
            elif digit == 1:
                total += left * d
                total += right+1
            else:
                total += (left+1) * d
            d *= 10
        return total

