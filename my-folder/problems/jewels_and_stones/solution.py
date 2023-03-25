class Solution:
    def numJewelsInStones(self, _jewels: str, stones: str) -> int:
        jewels = {}
        for j in _jewels:
            jewels[ord(j)] = True

        total = 0
        for s in stones:
            if ord(s) in jewels:
                total += 1
        
        return total