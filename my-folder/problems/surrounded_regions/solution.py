class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def block(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if board[r][c] != 'O':
                return
            board[r][c] = 'B'
            block(r-1, c)
            block(r+1, c)
            block(r, c-1)
            block(r, c+1)
        
        for r in 0, m-1:
            for c in range(n):
                block(r, c)
        
        for c in 0, n-1:
            for r in range(m):
                block(r, c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] != 'B':
                    board[r][c] = 'X'
                else:
                    board[r][c] = 'O'
            
        