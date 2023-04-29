class DataStream:

    def __init__(self, value: int, k: int):
        self.same = 0
        self.val = value
        self.k = k
        

    def consec(self, num: int) -> bool:
        if num == self.val:
            self.same += 1
        else:
            self.same = 0
        return self.same >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)