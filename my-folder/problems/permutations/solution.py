class Solution:
    def add_perm(self, prev: List[int]):
        if len(prev) == self.n:
            self.ret.append([*prev])
            return
        prev.append(100)
        for i in range(self.n):
            if self.nums[i] == -100:
                continue
            prev[-1] = self.nums[i]
            self.nums[i] = -100
            self.add_perm(prev)
            self.nums[i] = prev[-1]
        prev.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        self.n = len(nums)
        self.nums = nums
        self.add_perm([])
        return self.ret