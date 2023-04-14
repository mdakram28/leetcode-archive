class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s)-1
        j = len(t)-1

        bi = 0
        bj = 0

        while i>=0 and j>=0:
            # In each iteration skip backspaced characters
            while i >= 0:
                if s[i] == '#':
                    bi += 1
                elif bi > 0:
                    bi -= 1
                else:
                    break
                i -= 1
            
            while j >= 0:
                if t[j] == '#':
                    bj += 1
                elif bj > 0:
                    bj -= 1
                else:
                    break
                j -= 1
            # print(i, j)
            
            if i>=0 and j>=0:
                if s[i]!=t[j]:
                    return False
                i -= 1
                j -= 1
        
        while i >= 0:
            if s[i] == '#':
                bi += 1
            elif bi > 0:
                bi -= 1
            else:
                break
            i -= 1
        
        while j >= 0:
            if t[j] == '#':
                bj += 1
            elif bj > 0:
                bj -= 1
            else:
                break
            j -= 1
        
        return i==-1 and j==-1