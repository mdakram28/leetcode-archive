class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        coords = set((r,c) for r,c in coordinates)
        tocount = set()
        for r,c in coordinates:
            for dr, dc in (0, 0), (0, -1), (-1, 0), (-1, -1):
                nr,nc = r+dr, c+dc
                # print(nr, nc)
                if nr>=0 and nr<(m-1) and nc>=0 and nc<(n-1):
                    tocount.add((nr,nc))
        
        print(tocount)
        ans = [0]*5
        for r, c in tocount:
            count = 0
            for dr, dc in (0, 0), (0, 1), (1, 0), (1, 1):
                nr, nc = r+dr, c+dc
                if (nr,nc) in coords:
                    count += 1
            ans[count] += 1
        ans[0] = (m-1)*(n-1) - sum(ans)
        return ans