class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # extra = 0
        zeroes = 26
        freq = {chr(ord('a')+i): 0 for i in range(26)}

        for c in p:
            freq[c] += 1
            if freq[c] == 1:
                zeroes -= 1

        if len(p) > len(s):
            return []

        end = 0
        while end < (len(p)-1):
            c = s[end]
            freq[c] -= 1
            if freq[c] == 0:
                zeroes += 1
            elif freq[c] == -1:
                zeroes -= 1
            
            end += 1
        
        ret = []
        start = 0
        while end < len(s):
            c = s[end]
            freq[c] -= 1
            if freq[c] == 0:
                zeroes += 1
                if zeroes == 26:
                    ret.append(start)
            elif freq[c] == -1:
                zeroes -= 1

            c = s[start]
            freq[c] += 1
            if freq[c] == 0:
                zeroes += 1
            elif freq[c] == 1:
                zeroes -= 1
            
            start += 1
            end += 1

        return ret
