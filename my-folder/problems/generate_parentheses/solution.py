class Solution:
    def addAll(self, s, n_notopen, n_open, ret):
        if n_notopen == 0 and n_open == 0:
            ret.append(s)
        else:
            if n_open > 0:
                self.addAll(s + ')', n_notopen, n_open-1, ret)
            if n_notopen > 0:
                self.addAll(s + '(', n_notopen-1, n_open+1, ret)
            
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        self.addAll("", n, 0, ret)
        return ret