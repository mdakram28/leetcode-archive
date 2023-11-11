class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        f1 = defaultdict(int)
        f2 = defaultdict(int)
        for i, c in enumerate(s1):
            if i%2 == 0:
                f1[c] += 1
            else:
                f2[c] += 1
        for i, c in enumerate(s2):
            f = f1 if i%2 == 0 else f2
            if f[c] == 0:
                return False
            f[c] -= 1
        return True