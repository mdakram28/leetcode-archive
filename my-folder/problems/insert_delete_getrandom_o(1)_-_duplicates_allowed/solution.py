class RandomizedCollection:

    def __init__(self):
        self.vals = []
        self.idx = collections.defaultdict(dict)
        

    def insert(self, val: int) -> bool:
        not_present = not bool(self.idx[val])
        self.idx[val][len(self.vals)] = True
        self.vals.append(val)
        return not_present

    def remove(self, val: int) -> bool:
        not_present = not bool(self.idx[val])
        if not_present:
            return False
        repl = self.vals[-1]
        repl_idx = len(self.vals)-1
        if repl == val:
            self.vals.pop()
            del self.idx[repl][repl_idx]
            return True
        val_idx = next(iter(self.idx[val].keys()))
        del self.idx[repl][repl_idx]
        del self.idx[val][val_idx]

        self.vals[val_idx] = repl
        self.vals.pop()
        self.idx[repl][val_idx] = True
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()