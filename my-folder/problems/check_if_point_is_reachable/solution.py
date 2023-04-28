class Solution:
    def isReachable(self, X: int, Y: int) -> bool:
        t = math.gcd(X, Y)
        return t and (t-1)&t == 0
