from random import randint
class Solution:

    def __init__(self, m: int, n: int):
        self.flipped = []
        self.num_0 = m*n
        self.m = m
        self.n = n

    def flip(self) -> List[int]:
        num = randint(0, self.num_0-1)
        # print(f"Flip {num=}, {self.flipped=}")
        i = 0
        while i < len(self.flipped) and self.flipped[i] <= num:
            i += 1
            num += 1

        self.flipped.append(num)
        prev = num
        for j in range(i, len(self.flipped)):
            prev, self.flipped[j] = self.flipped[j], prev

        self.num_0 -= 1
        return num//self.n, num%self.n

    def reset(self) -> None:
        self.num_0 = self.m*self.n
        self.flipped.clear()
# 4
# 1, 3, 6
# 0, x, 2, x, 4, 5, x
# 

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()