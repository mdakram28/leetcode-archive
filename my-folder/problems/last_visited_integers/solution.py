class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        seen = []
        out = []
        c = 0
        for w in words:
            if w != "prev":
                c = 0
                seen.append(int(w))
            else:
                c += 1
                out.append(seen[-c] if c <= len(seen) else -1)
        return out