class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return chain.from_iterable(filter(bool, w.split(separator)) for w in words)