from sortedcontainers import SortedList
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapify(self.heap)
        if len(self.heap) < k:
            self.add = self.add_only
        else:
            self.add = self.add_and_rem
        while len(self.heap) > k:
            heappop(self.heap)

    def add_only(self, val: int) -> int:
        heappush(self.heap, val)
        self.add = self.add_and_rem
        return self.heap[0]
    
    def add_and_rem(self, val: int) -> int:
        heappush(self.heap, val)
        heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)