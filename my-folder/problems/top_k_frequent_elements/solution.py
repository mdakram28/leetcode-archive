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
        for f in range(len(nums)+1, 0, -1):
            ret.extend(revf[f])
            if len(ret) >= k:
                break
        
        return ret[:k]
        