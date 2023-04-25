class SmallestInfiniteSet:

    def __init__(self):
        self.right = 0
        self.f = {}
        self.heap = []
        # self.f = {}
        

    def popSmallest(self) -> int:
        if self.heap:
            ret = heappop(self.heap)
            self.f[ret] = 0
            return ret
        else:
            self.right += 1
            return self.right

    def addBack(self, num: int) -> None:
        if num <= self.right and not self.f.get(num):
            self.f[num] = 1
            heappush(self.heap, num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)