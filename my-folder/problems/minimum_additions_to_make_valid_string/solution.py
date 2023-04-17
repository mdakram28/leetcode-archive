class Solution:
    def addMinimum(self, word: str) -> int:
        prev = ord('c')
        total = 0
        for c in word:
            total += (ord(c) - prev - 1) % 3
            prev = ord(c)
        
        return total + (ord('a')-prev-1)%3