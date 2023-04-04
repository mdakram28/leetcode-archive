class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        f = collections.defaultdict(int)
        for n in nums:
            f[n] += 1

        ret = 0
        if k == 0:
            return sum(1 for k, v in f.items() if v > 1)
        
        for n in sorted(f.keys()):
            if (n-k) in f:
                ret += 1
        return ret