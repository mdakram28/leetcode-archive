def getLPS(s: str):
    lps = [0] * len(s)
    i = 1
    j = 0

    while i < len(s):
        if s[i] == s[j]:
            lps[i] = j+1
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = lps[j-1]
    
    return lps

class Solution:
    def longestDecomposition(self, text: str) -> int:
        
        @cache
        def get_max_splits(l):
            r = len(text)-l
            if l > r: return -float('inf')
            if l == r: return 0
            lps = getLPS(text[l:r])
            end = lps[-1]
            ans = 1
            # print(text[l:r], lps)
            while end > 0:
                # print(end)
                ans = max(ans, 2 + get_max_splits(l+end))
                end = lps[end-1]
            return ans
        
        ans = get_max_splits(0)
        return -1 if ans == -float('inf') else ans