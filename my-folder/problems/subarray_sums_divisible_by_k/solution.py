class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        f = collections.defaultdict(int)
        f[0] = 1
        t = 0
        for n in nums:
            t = (t+n)%k
            f[t] += 1
        
        ret = 0
        for val in f.values():
            ret += (val*(val-1)) // 2
        
        return ret