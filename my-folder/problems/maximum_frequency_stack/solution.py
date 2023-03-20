

class FreqStack:

    def __init__(self):
        self._st = [
            []
        ]
        self._freq = {}
        

    def push(self, val: int) -> None:
        new_freq = self._freq.get(val, 0) + 1
        self._freq[val] = new_freq

        if new_freq >= len(self._st):
            self._st.append([val])
        else:
            self._st[new_freq].append(val)

    def pop(self) -> int:
        val = self._st[-1].pop()
        if len(self._st[-1]) == 0:
            self._st.pop()
        self._freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()