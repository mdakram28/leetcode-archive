from fractions import Fraction

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2: return n
        max_count = 0
        f = defaultdict(int)
        for i, (x1, y1) in enumerate(points):
            f.clear()
            for x2, y2 in points[i+1:]:
                # if x1 == x2 and y1 == y2: continue
                frac = (y2-y1)/(x2-x1) if x1 != x2 else float('inf')
                f[frac] += 1
            if len(f) > 0:
                max_count = max(max_count, max(f.values()))
        
        return max_count+1
            
