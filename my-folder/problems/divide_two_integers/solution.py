class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q = 0
        sign = 1 if ((dividend > 0) == (divisor > 0)) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            m = 1
            while (divisor * m * 2) < dividend:
                m *= 2
            dividend -= divisor * m
            q += m
        return max(min(q * sign, 2**31 - 1), -2**31)