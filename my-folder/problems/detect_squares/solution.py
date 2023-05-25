class DetectSquares:

    def __init__(self):
        self.pbx = defaultdict(list)
        self.pf = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pbx[x].append(point)
        self.pf[(x,y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        for xt, yt in self.pbx[x]:
            if y == yt: continue
            a = abs(y-yt)
            if yt < y:
                ans += self.pf[(x-a, y)] * self.pf[(x-a, y-a)]
                ans += self.pf[(x+a, y)] * self.pf[(x+a, y-a)]
            else:
                ans += self.pf[(x-a, y)] * self.pf[(x-a, y+a)]
                ans += self.pf[(x+a, y)] * self.pf[(x+a, y+a)]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)