class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        count = {}
        ans = [0]*5
        ans[0] = (m-1)*(n-1)
        
        for r, c in coordinates:
            for dr, dc in (-1, -1), (-1, 0), (0, -1), (0, 0):
                r2, c2 = r+dr, c+dc
                if r2 < m-1 and r2 >= 0 and c2 < n-1 and c2 >= 0:
                    pc = count.get((r2, c2), 0)
                    ans[pc] -= 1
                    ans[pc+1] += 1
                    count[(r2, c2)] = pc+1
        
        return ans