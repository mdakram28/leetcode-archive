class Solution:
    def diffWaysToCompute(self, ex: str) -> List[int]:
        signfunc = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
        }
        @cache
        def calc(l, r):
            ret = []
            for i in range(l, r):
                if ex[i] in signfunc:
                    ret.extend(starmap(signfunc[ex[i]], product(calc(l, i),calc(i+1, r))))
            return ret or [int(ex[l:r])]
        
        return calc(0, len(ex))
