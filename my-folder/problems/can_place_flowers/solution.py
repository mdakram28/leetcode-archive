class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i, f in enumerate(flowerbed):
            if f == 0:
                if (i == 0 or flowerbed[i-1] == 0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                    n -= 1
                    flowerbed[i] = 1
        return n <= 0
                