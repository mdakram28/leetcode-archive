class Solution:
    def minimizedStringLength(self, s: str) -> int:
        f = defaultdict(int)
        for c in s:
            f[c] += 1
        
        return len(f.values())