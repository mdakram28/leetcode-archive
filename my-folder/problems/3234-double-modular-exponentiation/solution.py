class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        n = len(variables)
        ret = []
        for i, (a,b,c,m) in enumerate(variables):
            val = pow(pow(a, b, 10), c, m)
            if val == target:
                ret.append(i)
        
        return ret
