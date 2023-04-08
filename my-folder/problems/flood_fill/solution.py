class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        start_col = image[sr][sc]

        def dfs(r, c):
            nonlocal start_col
            if r<0 or r>=m or c<0 or c>=n or image[r][c] != start_col:
                return
            image[r][c] = color
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        if start_col == color:
            return image

        dfs(sr,sc)
        return image
