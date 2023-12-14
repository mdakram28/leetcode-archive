class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        diffCol = [2*sum(col)-m for col in zip(*grid)]

        for r, row in enumerate(grid):
            diffRow = 2*sum(row)-n
            for c in range(n):
                grid[r][c] = diffRow + diffCol[c]

        return grid
