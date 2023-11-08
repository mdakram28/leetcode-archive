class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return t != 1 if sx == fx and sy == fy else t >= max(abs(fy-sy), abs(fx-sx))
