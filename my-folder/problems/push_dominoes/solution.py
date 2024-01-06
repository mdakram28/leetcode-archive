class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        i = -1
        prev = 'L'
        ret = list(dominoes)
        ret.append("R")
        for j, d in enumerate(ret):
            if d == '.': continue
            if (prev, d) == ('R', 'L'):
                for k in range(i+1, (i+j+1)//2):
                    ret[k] = 'R'
                for k in range((i+j+2)//2, j):
                    ret[k] = 'L'
            elif prev == 'R':
                for k in range(i+1, j):
                    ret[k] = 'R'
            elif d == 'L':
                for k in range(i+1, j):
                    ret[k] = 'L'
            i = j
            prev = d
        ret.pop()
        return ''.join(ret)