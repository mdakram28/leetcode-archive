class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        pos = {}
        for r, row in enumerate(grid):
            val = sum(v<<d for d, v in enumerate(row))
            if val == 0:
                return [r]
            pos[val] = r
        
        allvals = list(pos.keys())
        for i in range(len(allvals)):
            for j in range(i+1, len(allvals)):
                if allvals[i] & allvals[j] == 0:
                    return sorted([pos[allvals[i]], pos[allvals[j]]])

        return []
