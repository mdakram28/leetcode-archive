class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        f1 = collections.defaultdict(int)
        f2 = collections.defaultdict(int)

        x = 0
        for i, (c1, c2) in enumerate(zip(secret, guess)):
            if c1 == c2:
                x += 1
            else:
                f1[c1] += 1
                f2[c2] += 1
        
        y = sum(min(f1[c], f2[c]) for c in f1.keys())

        return f"{x}A{y}B"
