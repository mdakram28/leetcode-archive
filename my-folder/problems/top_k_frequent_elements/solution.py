from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(lambda: 0)
        for n in nums:
            freq[n] += 1
        
        revf = defaultdict(list)
        for n, f in freq.items():
            revf[f].append(n)
        
        ret = []
        f = len(nums)
        while len(ret) < k:
            ret.extend(revf[f])
            f -= 1
        
        return ret
        