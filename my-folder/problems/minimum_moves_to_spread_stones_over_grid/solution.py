class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        stones = []
        spots = []
        for r, c in product(range(3), range(3)):
            if grid[r][c] > 1:
                stones.extend([(r,c) for _ in range(grid[r][c]-1)])
            elif grid[r][c] == 0:
                spots.append((r,c))
                
        def dist(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
        
        @cache
        def min_moves(stones_cnt, used_spots):
            if stones_cnt == 0: return 0
            
            ans = float('inf')
            for i in range(len(spots)):
                if used_spots&(1<<i): continue

                ans = min(
                    ans, 
                    min_moves(stones_cnt-1, used_spots|(1<<i)) + dist(stones[stones_cnt-1], spots[i])
                )
            
            return ans
        
        return min_moves(len(stones), 0)