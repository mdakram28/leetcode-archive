class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total = 0
        for c, sign in zip(str(n), cycle((1, -1))):
            total += sign*int(c)
            sign = -sign
        return total