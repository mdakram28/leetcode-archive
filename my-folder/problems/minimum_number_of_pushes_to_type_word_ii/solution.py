class Solution:
    def minimumPushes(self, word: str) -> int:
        f = sorted(Counter(word).values(), reverse=True)
        
        return sum(f[0:8]) + sum(f[8:16])*2 + sum(f[16:24])*3 + sum(f[24:32])*4
        