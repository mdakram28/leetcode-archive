import random
class Solution:

    def __init__(self, nums: List[int]):
        self.n = nums

    def reset(self) -> List[int]:
        return self.n

    def shuffle(self) -> List[int]:
        s = []
        rem = [*self.n]
        while rem:
            # print(rem)
            n = random.choice(rem)
            s.append(n)
            rem.remove(n)
        return s


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()