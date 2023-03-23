class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a = 1
        b = 1
        for i in range(1, n):
            a, b = b, (a+b)
        return b
