from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) > 0 and num <= -self.left[0]:
            heappush(self.left, -num)
            if len(self.left) > len(self.right):
                num2 = -heappop(self.left)
                heappush(self.right, num2)
        else:
            heappush(self.right, num)
            if len(self.right) > (len(self.left)+1):
                num2 = heappop(self.right)
                heappush(self.left, -num2)

    def findMedian(self) -> float:
        # print(self.left, self.right)
        if len(self.left) == len(self.right):
            return (self.right[0]-self.left[0])/2
        else:
            return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()