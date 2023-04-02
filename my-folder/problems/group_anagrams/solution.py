from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hash(w):
            h = 0
            for c in w:
                shift = 7*(ord(c)-ord('a'))
                h += (1 << shift)
            # print(bin(h))
            return h
        d = defaultdict(list)
        for w in strs:
            h = hash(w)
            d[h].append(w)
        
        return list(d.values())
