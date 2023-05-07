class FrequencyTracker:

    def __init__(self):
        self.f_to_nums = defaultdict(set)
        self.nums_to_f = defaultdict(int)

    def add(self, number: int) -> None:
        count = self.nums_to_f[number] = self.nums_to_f[number] + 1
        self.f_to_nums[count-1].discard(number)
        self.f_to_nums[count].add(number)

    def deleteOne(self, number: int) -> None:
        prev_count = self.nums_to_f[number]
        if prev_count == 0: return
        count = self.nums_to_f[number] = prev_count - 1
        self.f_to_nums[prev_count].discard(number)
        if count>0:
            self.f_to_nums[count].add(number)

    def hasFrequency(self, freq: int) -> bool:
        return bool(self.f_to_nums[freq])


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)