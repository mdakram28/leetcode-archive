class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        prev = []
        ans = []

        ans_l = 0
        op = 0
        for c in s:
            if c == '(':
                op += 1
                ans_l += 1
            elif c == ')':
                if op:
                    op -= 1
                    ans_l += 1
            else:
                ans_l += 1
        
        ans_l -= op
            
        def add_all(i, l ,r):
            if n-i < ans_l-len(prev):
                return
            if i == n:
                # Add only if prev is valid
                if l==r and len(prev) == ans_l: ans.append(''.join(prev))
                return
            
            if s[i] == '(' or s[i] == ')':
                next_i = i+1
                while next_i < n and s[next_i] == s[i]:
                    next_i += 1
                
                # prev_l = len(prev)
                add_all(next_i, l, r)
                
                if s[i] == '(':
                    for j in range(i, next_i):
                        prev.append('(')
                        l += 1
                        add_all(next_i, l, r)

                    for j in range(i, next_i):
                        prev.pop()
                        
                elif l > r:
                    max_i = min(next_i, i+l-r)
                    for j in range(i, max_i):
                        prev.append(')')
                        r += 1
                        add_all(next_i, l, r)
                    
                    for j in range(i, max_i):
                        prev.pop()

            else:
                prev.append(s[i])
                add_all(i+1, l, r)
                prev.pop()

        add_all(0, 0, 0)
        return ans