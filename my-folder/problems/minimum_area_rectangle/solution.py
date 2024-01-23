class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points = set(map(tuple, points))
        ans = float('inf')
        for (x1, y1), (x2, y2) in combinations(points, 2):
            if (x1, y2) in points and (x2, y1) in points:
                a = abs(x2-x1)*abs(y2-y1)
                if a != 0:
                    ans = min(ans, a)
        
        return 0 if ans == float('inf') else ans