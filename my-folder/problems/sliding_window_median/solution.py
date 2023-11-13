# from sortedcontainers import SortedList
class Heap():
    def __init__(self):
        self._q = []
        self._rem = defaultdict(int)
        self._remc = 0
    
    def __len__(self):
        return len(self._q)-self._remc

class MinHeap(Heap):
    def add(self, num):
        heappush(self._q, num)
    
    def remove(self, num):
        self._rem[num] += 1
        self._remc += 1
    
    def min(self):
        while self._q and self._rem[self._q[0]] > 0:
            self._rem[heappop(self._q)] -= 1
            self._remc -= 1
        return self._q[0] if self._q else None
    
    def pop(self):
        while self._q and self._rem[self._q[0]] > 0:
            self._rem[heappop(self._q)] -= 1
            self._remc -= 1
        return heappop(self._q) if self._q else None

class MaxHeap(Heap):
    def add(self, num):
        heappush(self._q, -num)
    
    def remove(self, num):
        self._rem[num] += 1
        self._remc += 1
    
    def max(self):
        while self._q and self._rem[-self._q[0]] > 0:
            self._rem[-heappop(self._q)] -= 1
            self._remc -= 1
        return -self._q[0] if self._q else None
        
    def pop(self):
        while self._q and self._rem[-self._q[0]] > 0:
            self._rem[-heappop(self._q)] -= 1
            self._remc -= 1
        return -heappop(self._q) if self._q else None

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = MaxHeap()
        right = MinHeap()

        def balance():
            while len(left) > len(right):
                right.add(left.pop())
            
            while len(right) > len(left)+1:
                left.add(right.pop())

        def add(num):
            if len(left) > 0 and num <= left.max():
                left.add(num)
            else:
                right.add(num)
            balance()

        def remove(num):
            if len(left)>0 and num <= left.max():
                left.remove(num)
            else:
                right.remove(num)
            balance()

        def median():
            if len(left) == len(right):
                return (left.max() + right.min())/2
            else:
                return right.min()

        ans = []
        for i, num in enumerate(nums):
            add(num)
            if i >= k:
                remove(nums[i-k])
            if i >= (k-1):
                ans.append(median())
        
        return ans
