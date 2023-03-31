class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_1s = abs(sum(sum(row) for row in grid))

        @cache
        def get_rc():
            for r in range(m):
                for c in range(n):
                    if grid[r][c]:
                        yield r, c

        # mul = 1
        # def set_dist(r, c, dist):
        #     if r < 0 or r>= m or c < 0 or c >= n:
        #         return
        #     if grid[r][c] != 1 and grid[r][c] <= dist:
        #         return
        #     grid[r][c] = dist
            
        #     set_dist(r-1, c, dist + 1)
        #     set_dist(r+1, c, dist + 1)
        #     set_dist(r, c-1, dist + 1)
        #     set_dist(r, c+1, dist + 1)
        
        island = 1
        def is_connected():
            nonlocal island
            def count(r, c):
                if r < 0 or r>= m or c < 0 or c >= n: return 0
                if grid[r][c] != island: return 0
                grid[r][c] = -island
                total = 1
                total += count(r-1, c)
                total += count(r+1, c)
                total += count(r, c-1)
                total += count(r, c+1)
                return total
            r, c = first_rc
            if not grid[r][c]:
                r, c = second_rc
            conn = count(r, c)
            island = -island
            return conn == num_1s

        if num_1s == 0:
            return 0
        elif num_1s == 1:
            return 1
        
        
        g = get_rc()
        first_rc = next(g)
        second_rc = next(g)

        if not is_connected():
            return 0
        elif num_1s == 2:
            return 2
        

        # skip = True
        num_1s -= 1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                # if skip:
                #     skip = False
                #     continue
                grid[r][c] = 0
                if not is_connected():
                    # print(f"Choke at {r}, {c}")
                    return 1
                grid[r][c] = island
                
                
        return 2

