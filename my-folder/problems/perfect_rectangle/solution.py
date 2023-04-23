class Solution:
    def isRectangleCover(self, rects: List[List[int]]) -> bool:
        area = 0
        corners = {}
        for x1, y1, x2, y2 in rects:
            area += (x2-x1)*(y2-y1)
            for corner in (x1, y1), (x1, y2), (x2, y1), (x2, y2):
                if corner not in corners:
                    corners[corner] = True
                else:
                    del corners[corner]
        
        if len(corners) != 4:
            return False

        c = set(corners.keys())
        x1, y1 = min(c)
        x2, y2 = max(c)

        return area == (x2-x1)*(y2-y1) and c == {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}