class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        rem = set(range(n))
        pos = 0
        i = 1
        while pos in rem:
            rem.remove(pos)
            pos = (pos + i*k) % n
            i += 1
        return [i+1 for i in rem]
            