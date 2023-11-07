from fractions import Fraction

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        return next((i for i,t in enumerate(sorted(d/s for d,s in zip(dist, speed))) if i>=t), len(dist))