from sortedcontainers import SortedList

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return max(min(i+1, c) for i, c in enumerate(sorted(citations, reverse=True)))
