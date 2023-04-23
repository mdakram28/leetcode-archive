class Solution:
            
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        prev = []
        def add_all(op, rem):
            if op == 0 and rem == 0:
                ret.append(''.join(prev))
                return
            if op:
                prev.append(')')
                add_all(op-1, rem)
                prev.pop()
            if rem:
                prev.append('(')
                add_all(op+1, rem-1)
                prev.pop()
        add_all(0, n)
        return ret