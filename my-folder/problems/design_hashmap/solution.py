from random import randint
from pprint import pprint

class MyHashMap:

    def __init__(self, size = 1, pref = ""):
        self.size = size
        self.store = [None] * self.size
        self.length = 0
        self.sum_keys = 0
        
    def hash(self, key: int):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        # print(f"{self.pref}Put {key=}, {value=}")
        i = self.hash(key)
        if self.store[i] is None:
            self.store[i] = (key, value)
            self.length += 1
            self.sum_keys += key
        elif isinstance(self.store[i], tuple):
            # print(f"{self.pref}Found tuple")
            prev_key, prev_val = self.store[i]
            if prev_key == key:
                self.store[i] = (key, value)
            else:
                nested_map = MyHashMap(randint(5, 20))
                nested_map.put(prev_key, prev_val)
                nested_map.put(key, value)
                self.store[i] = nested_map
                self.length += 1
                self.sum_keys += key
        else:
            # print(f"{self.pref}Found map")
            prev_length = self.store[i].length
            self.store[i].put(key, value)
            new_length = self.store[i].length
            self.length += new_length - prev_length
            if new_length != prev_length:
                self.sum_keys += key
        # print(f"{self.pref}{self.store}")

    # def __repr__(self, pref = ""):
    #     s = f"{" + "\n"
    #     for i in range(self.size):
    #         if self.store[i] is None:
    #             continue
    #         elif isinstance(self.store[i], tuple):
    #             k,v = self.store[i]
    #             s += f"{pref}{k}: {v}\n"
    #         else:


    def get(self, key: int) -> int:
        # print(f"{self.pref}Get {key=}, {self.store=}")
        i = self.hash(key)
        if self.store[i] is None:
            return -1
        elif isinstance(self.store[i], tuple):
            prev_key, prev_val = self.store[i]
            if prev_key == key:
                return prev_val
            else:
                return -1
        else:
            return self.store[i].get(key)

    def remove(self, key: int) -> None:
        i = self.hash(key)
        if self.store[i] is None:
            return
        elif isinstance(self.store[i], tuple):
            prev_key, prev_val = self.store[i]
            if prev_key == key:
                self.store[i] = None
                self.length -= 1
                self.sum_keys -= key
        else:
            prev_length = self.store[i].length
            self.store[i].remove(key)
            new_length = self.store[i].length
            self.length -= prev_length-new_length
            if prev_length != new_length:
                self.sum_keys -= key
            if new_length == 1:
                rem_key = self.store[i].sum_keys
                self.store[i] = (rem_key, self.store[i].get(rem_key))
            elif new_length == 0:
                self.store[i] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)