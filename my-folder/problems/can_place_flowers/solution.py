from math import ceil
class Solution:
    def canPlaceFlowers(self, flowers: List[int], place: int) -> bool:
        
        i = 0
        n = len(flowers)
        slots = 0
        while i < n:
            if flowers[i] == 1:
                i += 1 
            else:
                start = i
                while i < n and flowers[i] == 0:
                    i += 1
                num = i-start
                slots += (num-1)//2
                if i == n and start == 0:
                   slots += 1
                elif num%2 == 0 and (i == n or start == 0):
                    slots += 1
        
        return place <= slots