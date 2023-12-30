class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        f = defaultdict(int)
        for word in words:
            for c in word:
                f[c] += 1
        return all(count%len(words) == 0 for count in f.values())