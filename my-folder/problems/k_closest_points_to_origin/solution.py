class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i in range(len(points)):
            x, y = points[i]
            dist.append((i, x*x + y*y))
        
        dist.sort(key=lambda d: d[1])
        for i in range(k):
            dist[i] = points[dist[i][0]]
        return dist[:k]