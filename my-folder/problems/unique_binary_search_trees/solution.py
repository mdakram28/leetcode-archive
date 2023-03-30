class Solution:
    def numTrees(self, n: int) -> int:
        vals = [1]
        for i in range(1, n+1):
            t = 0
            for j in range(i):
                t += vals[j]*vals[i-j-1]
            vals.append(t)
        return vals[-1]