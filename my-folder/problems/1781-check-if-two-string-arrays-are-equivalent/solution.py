class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return all(a==b for a,b in zip_longest(chain.from_iterable(word1), chain.from_iterable(word2)))
