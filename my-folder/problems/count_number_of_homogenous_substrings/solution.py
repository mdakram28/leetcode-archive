class Solution:
    def countHomogenous(self, s: str) -> int:
        return sum(i+1-(st := 0 if i == 0 else st if s[i]==s[i-1] else i) for i in range(len(s))) % (10**9+7)

        # p = None
        # start = 0
        # t = 0
        # mod = 10**9 + 7
        # for i, c in enumerate(s):
        #     if p != c:
        #         n = (i-start)
        #         t = (t + (n*(n+1))//2) % mod
        #         p = c
        #         start = i
        # n = (len(s)-start)
        # t = (t + (n*(n+1))//2) % mod
        # return t