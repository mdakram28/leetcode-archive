class MinStack:

    def __init__(self):
        self.st = []
        self.min_idx = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.min_idx) == 0:
            self.min_idx.append(0)
        elif val < self.st[self.min_idx[-1]]:
            self.min_idx.append(len(self.st)-1)
        else:
            self.min_idx.append(self.min_idx[-1])

    def pop(self) -> None:
        self.min_idx.pop()
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.st[self.min_idx[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()