class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        return sum(piles[i*2+1] for i in range(len(piles)//3))