class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        rep = {}
        grid = [[1]*col for r in range(row)]

        # First row has the same group
        r = 0
        for c in range(col):
            rep[(r, c)] = (0, 0)
        # Last row has the same group
        r = row-1
        for c in range(col):
            rep[(r, c)] = (r ,0)
        # All other cells are separate
        for r in range(1, row-1):
            for c in range(col):
                rep[(r, c)] = (r, c)

        def get_rep(node):
            r = node
            while rep[r] != r:
                r = rep[r]
            at = node
            while at != r:
                rep[at], at = r, rep[at]
            return r
        
        def merge(n1, n2):
            r1 = get_rep(n1)
            r2 = get_rep(n2)
            rep[r1] = r2

        # Iterate from the last adding 1 land cell each time
        for i, (r, c) in enumerate(cells[::-1]):
            r-=1
            c-=1
            grid[r][c] = 0
            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=row or nc<0 or nc>=col or grid[nr][nc] == 1:
                    continue
                # Connect this cell to neighbour cell
                merge((r, c), (nr, nc))
            
            # If the group of top and bottom row has become same
            # They are now connected
            r_top = get_rep((0, 0))
            r_bottom = get_rep((row-1, 0))
            if r_top == r_bottom:
                return len(cells)-1-i
        
        # Should never reach
        return 0
