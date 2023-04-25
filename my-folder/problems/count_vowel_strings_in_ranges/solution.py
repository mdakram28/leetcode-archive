class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        VOWELS = "aeiou"
        pref = [0]
        total = 0
        for w in words:
            if w[0] in VOWELS and w[-1] in VOWELS:
                total += 1
            pref.append(total)
        
        ans = []
        for l, r in queries:
            ans.append(pref[r+1] - pref[l])
        return ans