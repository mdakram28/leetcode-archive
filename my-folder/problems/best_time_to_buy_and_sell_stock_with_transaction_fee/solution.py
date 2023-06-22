class Solution:
    def maxProfit(self, prices: List[int], f: int) -> int:
        return reduce(lambda ab, p: (max(ab[0], ab[1]+p-f), max(ab[0]-p, ab[1])), prices, (0, -float('inf')))[0]