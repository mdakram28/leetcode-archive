class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        return ({0:1,1:2,2:2}.get(n) or (self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)+1))-1