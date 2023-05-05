from sortedcontainers import SortedList

class Allocator:

    def __init__(self, n: int):
        self.sl = SortedList()
        self.n = n
        self.sl.add((n, n, None))

    def allocate(self, size: int, mID: int) -> int:
        pos = 0
        i = 0
        while i<len(self.sl):
            if (pos+size) <= self.sl[i][0]:
                self.sl.add((pos, pos+size, mID))
                # print(size, mID, self.sl)
                return pos
            pos = self.sl[i][1]
            i += 1
        return -1

    def free(self, mID: int) -> int:
        ans = 0
        to_remove = []
        for t in self.sl:
            if t[2] == mID:
                ans += t[1]-t[0]
                to_remove.append(t)
        for t in to_remove:
            self.sl.remove(t)
        return ans


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)