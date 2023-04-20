class Solution:
    def appealSum(self, s: str) -> int:
        total = 0
        prev = 0
        last_idx = {}
        for i,c in enumerate(s):
            prev += i-last_idx.get(c, -1)
            # print(f"{i=}, count={prev}")
            total += prev
            last_idx[c] = i
        return total