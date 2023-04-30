class Solution:
    def pivotInteger(self, n: int) -> int:
        ans = math.sqrt((n*(n+1))//2)
        return int(ans) if int(ans) == ans else -1