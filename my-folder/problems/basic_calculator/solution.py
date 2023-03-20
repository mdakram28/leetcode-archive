class Solution:
    def calculate(self, s: str) -> int:
        global i
        i = 0
        def eval_expr():
            global i
            res = 0
            operation = None
            while i<len(s):
                if s[i] == '(':
                    i += 1
                    val = eval_expr()
                    if operation == '-':
                        res -= val
                    else:
                        res += val
                elif s[i] == '+' or s[i] == '-':
                    operation = s[i]
                elif s[i] == ' ':
                    pass
                elif s[i] == ')':
                    return res
                else:
                    val = 0
                    while i < len(s) and s[i].isnumeric():
                        val = val*10 + (ord(s[i]) - ord('0'))
                        i += 1
                    i -= 1
                    if operation == '-':
                        res -= val
                    else:
                        res += val 
                i += 1
            return res
        return eval_expr()
