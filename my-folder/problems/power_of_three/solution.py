class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        l = math.log(n)/math.log(3)
        return 3**round(l) == n