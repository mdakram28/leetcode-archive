class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1
        
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i
        
        return -1