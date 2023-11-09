class StockSpanner:

    def __init__(self):
        self.sl = [(float('inf'), -1)]
        self.d = 0

    def next(self, price: int) -> int:
        while self.sl and self.sl[-1][0] <= price:
            self.sl.pop()
        ret = self.d-self.sl[-1][1]
        self.sl.append((price, self.d))
        self.d += 1
        return ret


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)