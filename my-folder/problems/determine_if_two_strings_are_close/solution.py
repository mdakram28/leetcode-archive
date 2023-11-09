class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f1 = defaultdict(int)
        f2 = defaultdict(int)
        for c in word1:
            f1[c] += 1

        for c in word2:
            f2[c] += 1

        return set(f1.keys()) == set(f2.keys()) and sorted(f1.values()) == sorted(f2.values())