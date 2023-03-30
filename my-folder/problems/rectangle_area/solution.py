class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def overlap(a1, a2, b1, b2):
            return max(min(a2, b2) - max(a1, b1), 0)
        
        over_x = overlap(ax1, ax2, bx1, bx2)
        over_y = overlap(ay1, ay2, by1, by2)
        # print(over_x, over_y)

        area_a = (ax2-ax1) * (ay2-ay1)
        area_b = (bx2-bx1) * (by2-by1)
        return area_a + area_b - over_x*over_y