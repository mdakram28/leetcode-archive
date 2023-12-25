class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        b = 1
        a = 1 if s[-1] != '0' else 0

        for i in range(n-2, -1, -1):
            if s[i] == '0':
                a, b = 0, a
            elif s[i] == '1' or (s[i]=='2' and s[i+1] <= '6'):
                a, b = a+b, a
            else:
                a, b = a, a
        
        return a
                
            