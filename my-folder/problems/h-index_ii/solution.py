class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for h in range(1001, -1, -1):
            if len(citations)-bisect_left(citations, h) >= h:
                return h
        return -1