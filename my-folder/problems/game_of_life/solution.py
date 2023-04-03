class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        # def neighbour(r, c):
        
        # for r in range(m):
        #     for c in range(n):
        #         print(board[r][c], end="\t")
        #     print()
        # print("-----------------------------------")
        for r in range(m):
            for c in range(n):
                count = 0
                if r > 0 and board[r-1][c]&1:
                    count += 1
                if c > 0 and board[r][c-1]&1:
                    count += 1
                if r < (m-1) and board[r+1][c]&1:
                    count += 1
                if c < (n-1) and board[r][c+1]&1:
                    count += 1
                
                if r > 0 and c > 0 and board[r-1][c-1]&1:
                    count += 1
                if r > 0 and c < (n-1) and board[r-1][c+1]&1:
                    count += 1
                if r < (m-1) and c < (n-1) and board[r+1][c+1]&1:
                    count += 1
                if r < (m-1) and c > 0 and board[r+1][c-1]&1:
                    count += 1

                # print(count, end="\t")
                val = board[r][c]
                if val:
                    if count < 2 or count > 3:
                        val = 0
                else:
                    if count == 3:
                        val = 1
                
                board[r][c] |= val << 1
            # print()
        
        for r in range(m):
            for c in range(n):
                board[r][c] >>= 1