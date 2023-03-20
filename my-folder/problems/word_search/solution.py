class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        def find_recurse(r, c, i):
            if i >= len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if visited[r][c] or board[r][c] != word[i]:
                return False
            visited[r][c] = True
            
            i += 1
            if find_recurse(r+1, c, i):
                return True
            if find_recurse(r-1, c, i):
                return True
            if find_recurse(r, c+1, i):
                return True
            if find_recurse(r, c-1, i):
                return True
            
            visited[r][c] = False
            return False
        
        for r in range(m):
            for c in range(n):
                if find_recurse(r, c, 0):
                    return True
        
        return False