class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        isvowel = [c in 'aeiou' for c in s]
        
        count = 0
        for l in range(len(s)):
            v = 0
            c = 0
            for r in range(l, len(s)):
                if isvowel[r]: v += 1
                else: c += 1
                if v==c and (v*c)%k == 0:
                    count += 1
        
        return count