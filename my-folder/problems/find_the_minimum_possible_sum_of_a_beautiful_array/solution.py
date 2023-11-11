class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        r = (target-1)//2
        l = math.ceil((target-1)/2)
        f = target
        mod = 10**9+7
        if n <= l:
            return ((n*(n+1))//2)%mod
        b = target+n-l-1
        target-=1
        return (((l*(l+1))//2)%mod + ((b*(b+1))//2)%mod - ((target*(target+1))//2)%mod)%mod