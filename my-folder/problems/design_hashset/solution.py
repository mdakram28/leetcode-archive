class MyHashSet:

    def __init__(self):
        self.l = 1001
        self.s = [[] for _ in range(self.l)]
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.s[key%self.l].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.s[key%self.l].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.s[key%self.l]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)