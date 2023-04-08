class Solution:
    def convert(self, s: str, R: int) -> str:
        if R == 1:
            return s
        ret = []
        ls = len(s)
        lg = (2*R - 2)

        i = 0
        while i < ls:
            ret.append(s[i])
            i += lg
        
        for r in range(1, R-1):
            i = r
            while i<ls:
                ret.append(s[i])
                i += lg
                if i-(2*r) < ls:
                    ret.append(s[i-(2*r)])
        
        i = R-1
        while i<ls:
            ret.append(s[i])
            i += lg
        
        return ''.join(ret)