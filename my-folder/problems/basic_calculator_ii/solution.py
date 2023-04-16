class Solution:
    def calculate(self, s: str) -> int:
        
        n = len(s)
        i = 0

        PLUS = 1
        MINUS = -1
        MUL = 2
        DIV = 3

        def get_token():
            nonlocal i
            while i < n and s[i] == ' ':
                i += 1
            
            if i == n:
                return None, None

            symb = PLUS
            if s[i] == '-': symb = MINUS
            elif s[i] == '*': symb = MUL
            elif s[i] == '/': symb = DIV

            while i<n and s[i] < '0':
                i += 1
            
            num = 0
            while i < n and '0' <= s[i] <= '9':
                num = num*10 + (ord(s[i]) - ord('0'))
                i += 1
            
            return symb, num
        
        ans = 0
        last_val = 0
        while True:
            
            while i < n and s[i] == ' ': i += 1
            
            if i == n: break

            symb = PLUS
            if s[i] == '-': symb = MINUS
            elif s[i] == '*': symb = MUL
            elif s[i] == '/': symb = DIV

            while i<n and s[i] < '0': i += 1
            
            num = 0
            while i < n and '0' <= s[i] <= '9':
                num = num*10 + (ord(s[i]) - ord('0'))
                i += 1

            if symb == MUL:
                last_val *= num
            elif symb == DIV:
                last_val = int(last_val/num)
            else:
                ans += last_val
                last_val = symb*num
        
        return ans + last_val






