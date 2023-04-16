class Solution:
    def canCross(self, stones: List[int]) -> bool:
        prev = {stone: set() for stone in stones}
        prev[0].add(0)

        for stone in stones:
            for p in prev[stone]:

                for n in p-1, p, p+1:
                    if n and stone+n in prev:
                        prev[stone+n].add(n)

        return bool(prev[stones[-1]])