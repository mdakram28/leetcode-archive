class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        free_c = [True] * n
        free_d1 = [True] * (n + n-1)
        free_d2 = [True] * (n + n-1)

        board = [["." for c in range(n)] for r in range(n)]
        boards = []

        def solve(r):
            if r >= n:
                boards.append([''.join(row) for row in board])
                # return 1
            # total = 0
            for c in range(n):
                d1 = r-c + (n-1)
                d2 = r-(n-c-1) + (n-1)
                if free_c[c] and free_d1[d1] and free_d2[d2]:
                    free_c[c] = False
                    free_d1[d1] = False
                    free_d2[d2] = False
                    board[r][c] = 'Q'
                    solve(r+1)
                    board[r][c] = '.'
                    free_c[c] = True
                    free_d1[d1] = True
                    free_d2[d2] = True
            # return total

        solve(0)
        return boards