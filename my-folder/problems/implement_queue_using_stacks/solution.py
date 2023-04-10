class MyQueue:

    def __init__(self):
        self.front_st = []
        self.back_st = []
        

    def push(self, x: int) -> None:
        if not self.back_st:
            while self.front_st:
                self.back_st.append(self.front_st.pop())
        self.back_st.append(x)


    def pop(self) -> int:
        if not self.front_st:
            while self.back_st:
                self.front_st.append(self.back_st.pop())
        return self.front_st.pop()
        

    def peek(self) -> int:
        if not self.front_st:
            while self.back_st:
                self.front_st.append(self.back_st.pop())
        return self.front_st[-1]
        

    def empty(self) -> bool:
        return not self.front_st and not self.back_st
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()