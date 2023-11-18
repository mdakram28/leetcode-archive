class MajorityChecker:
    def __init__(self, arr):
        self.arr = arr
        self.dict1 = defaultdict(list)

        for i,x in enumerate(arr):
            self.dict1[x].append(i)

    def query(self, left, right, threshold):
        for _ in range(10):
            k = random.randint(left,right)
            res = self.arr[k]
            lo = bisect.bisect_left(self.dict1[res],left)
            hi = bisect.bisect_right(self.dict1[res],right)
            if hi-lo >= threshold: return res

        return -1





        