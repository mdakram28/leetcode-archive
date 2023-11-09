class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowcnt = defaultdict(int)
        for row in grid:
            rowcnt[tuple(row)] += 1

        ans = 0
        for c in range(len(grid[0])):
            col = tuple(grid[r][c] for r in range(len(grid)))
            ans += rowcnt[col]
        return ans
