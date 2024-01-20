class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0]*(k+1)
        self.front = 0
        self.back = 0
        self.size = k+1

    def enQueue(self, value: int) -> bool:
        if (self.back+1)%self.size == self.front:
            return False
        self.data[self.back] = value
        self.back = (self.back+1)%self.size
        return True

    def deQueue(self) -> bool:
        if self.front == self.back:
            return False
        self.front = (self.front+1)%self.size
        return True

    def Front(self) -> int:
        if self.front == self.back:
            return -1
        return self.data[self.front]

    def Rear(self) -> int:
        if self.back == self.front:
            return -1
        return self.data[(self.back-1)%self.size]

    def isEmpty(self) -> bool:
        return self.front == self.back

    def isFull(self) -> bool:
        return (self.back+1)%self.size == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()