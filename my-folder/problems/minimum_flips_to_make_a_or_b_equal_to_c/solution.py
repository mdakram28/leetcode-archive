class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return sum(((x|y)^z) * abs(z - (x+y)) for x, y, z in (((a>>i)&1, (b>>i)&1, (c>>i)&1) for i in range(len(bin(a|b|c)))))