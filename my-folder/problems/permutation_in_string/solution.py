class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        f = defaultdict(int)
        for c in s1:
            f[c] += 1

        f2 = defaultdict(int)
        end = 0
        for start in range(n2):
            while end < n2 and f2[s2[end]] < f[s2[end]]:
                f2[s2[end]] += 1
                end += 1
            
            if (end-start) == n1: return True
            if end == n2: return False

            if f2[s2[start]] > 0:
                f2[s2[start]] -= 1
            else:
                end += 1
            
            # print(start, end, {k:v for k,v in f2.items() if v})
        
        return False
        