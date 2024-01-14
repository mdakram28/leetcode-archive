def getLPS(s: str):
    lps = [0] * len(s)
    i = 1
    j = 0

    while i < len(s):
        if s[i] == s[j]:
            i += 1
            j += 1
            lps[i] = j
        elif j == 0:
            i += 1
        else:
            j = lps[j]
    
    return lps

def all_matches(s, a):
    offset = 0
    while offset < len(s):
        ind = s.find(a, offset)
        if ind == -1: return
        yield ind
        offset = ind+1

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