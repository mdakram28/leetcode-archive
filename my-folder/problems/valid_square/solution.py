class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        def dist(p1, p2):
            return (p2[1]-p1[1])**2 + (p2[0]-p1[0])**2
        
        d = [
            dist(p1, p2),
            dist(p1, p3),
            dist(p1, p4),
            dist(p2, p3),
            dist(p2, p4),
            dist(p3, p4)
        ]

        side = min(d)
        diag = max(d)
        return side and diag and d.count(side) == 4 and d.count(diag) == 2
        
            