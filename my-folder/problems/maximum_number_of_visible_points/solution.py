class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x0, y0 = location
        angles = [math.atan2(x1-x0, y1-y0)*180/math.pi for x1, y1 in points if x1!=x0 or y1!=y0]
        angles.sort()
        # print(angles)

        end = 0
        n = len(angles)
        max_points = 0
        for start in range(n):
            while (angles[end%n] - angles[start])%360 <= angle and end < n+start:
                end += 1
            max_points = max(max_points, end-start)

        return max_points + (len(points)-len(angles))