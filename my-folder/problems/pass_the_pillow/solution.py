class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        r = (time-1) // (n-1)
        offset = time - r*(n-1)
        if r % 2:
            return n - offset
        else:
            return 1 + offset