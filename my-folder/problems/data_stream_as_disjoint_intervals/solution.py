from sortedcontainers import SortedSet
class SummaryRanges:

    def __init__(self):
        self.ss = SortedSet()

    def addNum(self, value: int) -> None:
        self.ss.add(value)

    def getIntervals(self) -> List[List[int]]:
        ret = []
        start = None
        prev = None
        for num in self.ss:
            if num-1 == prev:
                prev = num
                continue
            if start is not None:
                ret.append([start, prev])
            start = num
            prev = num
        if start is not None:
            ret.append([start, prev])
        return ret



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()