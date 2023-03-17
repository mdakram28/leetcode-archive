class Solution:
    def add_cand(self, target, i):
        # print(f"{i=}, {target=}")

        if target == 0:
            self.ret.append([*self.l])
            return
        elif i >= self.len_cand:
            return

        target_rem = target
        while target_rem >= 0:
            self.add_cand(target_rem, i+1)
            self.l.append(self.cand[i])
            target_rem -= self.cand[i]
        del self.l[-((target // self.cand[i]) + 1):]

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.cand = candidates
        self.ret = []
        self.len_cand = len(candidates)
        self.l = []

        self.add_cand(target, 0)

        return self.ret
            
