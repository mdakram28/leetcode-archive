class TimeMap:

    def __init__(self):
        self.store: Dict[str, List[tuple(int, str)]] = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store[key]
        l = 0
        r = len(vals)
        # 1,2,3,4, 
        while l < r:
            mid = (l+r) // 2
            if vals[mid][0] <= timestamp:
                l = mid+1
            else:
                r = mid
        if (l-1) < 0:
            return ""
        else:
            return vals[l-1][1]

            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)