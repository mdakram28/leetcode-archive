class Solution:
    def numberOfWays(self, corridor: str) -> int:
        prev = None
        total = 1
        j = 0
        for j, pos in enumerate((i for i, c in enumerate(corridor) if c == 'S')):
            if j%2 == 0 and prev is not None:
                total = (total*(pos-prev))%(10**9+7)
            prev = pos
        
        if j%2 == 0:
            return 0
        
        return total
