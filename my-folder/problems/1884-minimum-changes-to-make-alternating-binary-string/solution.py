class Solution:
    def minOperations(self, s: str) -> int:
        a = sum(1 for a, b in zip(cycle('01'), s) if a == b)
        return min(a, len(s)-a)
