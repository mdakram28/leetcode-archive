class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        notfound = set(range(1, n*n+1))
        a = None
        
        for row in grid:
            for val in row:
                if val not in notfound:
                    a = val
                else:
                    notfound.discard(val)
        
        return [a, list(notfound)[0]]
