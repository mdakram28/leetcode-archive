class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        
        if n3 != (n1+n2): return False

        @cache
        def can_make(i, j):
            if i == n1 and j == n2: return True
            elif i == n1: return s2[j] == s3[i+j] and can_make(i, j+1)
            elif j == n2: return s1[i] == s3[i+j] and can_make(i+1, j)
            else:
                return (
                    (s1[i] == s3[i+j] and can_make(i+1, j))
                    or 
                    (s2[j] == s3[i+j] and can_make(i, j+1))
                )
        
        return can_make(0, 0)