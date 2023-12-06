class Solution:
    def totalMoney(self, n: int) -> int:
        W = n//7
        d = n%7
        return (7*W*(W-1))//2 + 28*W + (d*(d+1))//2 + W*d
