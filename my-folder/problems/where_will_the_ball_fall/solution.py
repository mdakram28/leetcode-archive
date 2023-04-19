class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ret = []
        m = len(grid)
        n = len(grid[0])
        for row in grid:
            row.append(-1)
            row.append(1)

        for pos in range(n):
            for r in range(m):
                neigh = pos+1 if grid[r][pos]==1 else pos-1
                if grid[r][pos]*grid[r][neigh] == -1:
                    pos = -1
                    break
                pos = neigh
                
            ret.append(pos)
        return ret
            