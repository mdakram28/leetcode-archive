class Solution:
    def minDeletions(self, s: str) -> int:
        f = collections.defaultdict(int)
        for c in s:
            f[c] += 1
        
        f = sorted(f.values())

        counts = {}

        for c in f:
            while c and c in counts:
                c -= 1
            counts[c] = True
        # print(counts)
        return sum(f) - sum(counts.keys())