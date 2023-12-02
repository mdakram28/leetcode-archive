class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        f = Counter(chars)
        ans = 0
        for w in words:
            f2 = defaultdict(int)
            for c in w:
                f2[c] += 1
                if f2[c] > f[c]:
                    break
            else:
                ans += len(w)
        
        return ans
