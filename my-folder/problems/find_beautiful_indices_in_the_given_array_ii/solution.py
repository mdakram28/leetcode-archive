def getLPS(s: str):
    lps = [0] * len(s)
    i = 1
    j = 0

    while i < len(s):
        if s[i] == s[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j == 0:
            lps[i] = 0
            i += 1
        else:
            j = lps[j-1]
    
    return lps

def all_matches(s, a):
    lps = getLPS(a)
    
    i = 0
    j = 0
    while (len(s) - i) >= (len(a) - j):
        if a[j] == s[i]:
            i += 1
            j += 1
 
        if j == len(a):
            yield i-j
            j = lps[j-1]
        elif i < len(s) and a[j] != s[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

class Solution:
        
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ret = []
        iter_a = iter(all_matches(s, a))
        iter_b = list(all_matches(s, b))
        # print(iter_a, iter_b)
        for i in iter_a:
            j = bisect_left(iter_b, i)
            if j < len(iter_b) and abs(iter_b[j]-i) <= k:
                ret.append(i)
            elif j > 0 and abs(iter_b[j-1]-i) <= k:
                ret.append(i)
        return ret