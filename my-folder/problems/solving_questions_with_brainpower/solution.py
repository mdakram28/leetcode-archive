class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        prev = [0]
        for p, b in questions[::-1]:
            prev.append(max(prev[-1], p + prev[max(len(prev)-b-1, 0)]))
        return prev[-1]