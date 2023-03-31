from random import uniform
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        x = uniform(0, 2) - 1
        y = uniform(0, 2) - 1
        r = x*x + y*y
        while r >= 1:
            x = uniform(0, 2) - 1
            y = uniform(0, 2) - 1
            r = x*x + y*y
        return x*self.r + self.x, y*self.r + self.y


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()