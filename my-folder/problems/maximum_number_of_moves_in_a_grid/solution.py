class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        d = [[1] * n for _ in range(m)]
        
        for c in range(n-2, -1, -1):
            for r in range(m):
                d[r][c] = max(
                    (d[r-1][c+1] + 1) if r > 0 and   grid[r-1][c+1] > grid[r][c] else 1,
                    (d[r][c+1]   + 1)   if             grid[r][c+1]   > grid[r][c] else 1,
                    (d[r+1][c+1] + 1) if r < m-1 and grid[r+1][c+1] > grid[r][c] else 1,
                )
        # print('\n'.join(map(str, d)))
#         @cache
#         def max_rc(r, c):
#             if c == n or r < 0 or r >= m: return 0
#             if c == n-1: return 1
#             val = grid[r][c]
#             ret = max(
#                 (grid[r-1][c+1] + 1) if r > 0 and grid[r-1][c+1] > val else 0,
#                 (grid[r][c+1] + 1) if grid[r][c+1] > val else 0,
#                 (grid[r+1][c+1] + 1) if r < n-1 and grid[r+1][c+1] > val else 0,
#             )
            
#             print(r, c, ret)
#             return ret
        
        return max(d[r][0] for r in range(m))-1