class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i][i] = True
        for i, row in enumerate(grid):
            if all(row):
                return i
        return 0