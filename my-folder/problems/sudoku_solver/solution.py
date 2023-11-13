class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rowrem = [[True]*10 for r in range(9)]
        colrem = [[True]*10 for r in range(9)]
        blockrem = {(a,b): [True]*10 for a in range(3) for b in range(3)}

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': continue
                num = int(board[r][c])
                block = (r//3, c//3)
                rowrem[r][num] = False
                colrem[c][num] = False
                blockrem[block][num] = False
        
        def solve(r, c):
            if r == 9: return True
            if board[r][c] != '.': return solve(r+(c+1)//9, (c+1)%9)
            
            block = (r//3, c//3)
            brem = blockrem[block]
            for num in range(1, 10):
                if rowrem[r][num] and colrem[c][num] and brem[num]:
                    board[r][c] = num
                    rowrem[r][num] = False
                    colrem[c][num] = False
                    brem[num] = False
                    if solve(r+(c+1)//9, (c+1)%9):
                        return True
                    rowrem[r][num] = True
                    colrem[c][num] = True
                    brem[num] = True

            board[r][c] = '.'
            return False
        
        solve(0, 0)

        for r in range(9):
            for c in range(9):
                board[r][c] = str(board[r][c])