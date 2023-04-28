class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        f1 = defaultdict(int)
        f2 = defaultdict(int)
        
        for c in word1:
            f1[c] += 1
        for c in word2:
            f2[c] += 1
        
        
        l1 = list(f1.keys())
        l2 = list(f2.keys())
        
        u1 = len(l1)
        u2 = len(l2)
        
        for c1 in l1:
            for c2 in l2:
                if c1 == c2:
                    if u1 == u2:
                        return True
                    continue
                d1, d2 = 0, 0
                if f1[c1] == 1:
                    d1 -= 1
                if f1[c2] == 0:
                    d1 += 1
                if f2[c1] == 0:
                    d2 += 1
                if f2[c2] == 1:
                    d2 -= 1
                if u1+d1 == u2+d2:
                    return True
                
        
        return False
        