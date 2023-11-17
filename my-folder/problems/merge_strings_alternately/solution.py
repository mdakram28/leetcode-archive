class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        for a, b in zip_longest(word1, word2):
            if a is not None:
                ans.append(a)
            if b is not None:
                ans.append(b)
        return ''.join(ans)