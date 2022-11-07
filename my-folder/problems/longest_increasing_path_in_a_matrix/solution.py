class Solution:
    def setDepths(self, r,c, newDepth=1, minValue=0):
        if r<0 or c<0 or r>=self.rows or c>=self.cols:
            return
        if self.depths[r][c] >= newDepth or self.matrix[r][c] < minValue:
            return
        self.depths[r][c] = newDepth
        self.maxDepth = max(self.maxDepth, newDepth)
        
        minValue = self.matrix[r][c]+1
        newDepth = newDepth+1
        self.setDepths(r-1,c, newDepth, minValue)
        self.setDepths(r+1,c, newDepth, minValue)
        self.setDepths(r,c-1, newDepth, minValue)
        self.setDepths(r,c+1, newDepth, minValue)
        
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.depths = [[0]*self.cols for r in range(self.rows)]
        self.maxDepth = 1
        for r in range(self.rows):
            for c in range(self.cols):
                self.setDepths(r,c)
                # print(f"Set depths at ({r}, {c})")
                # print("\n".join(["\t".join([str(c) for c in r]) for r in self.depths]))

        return self.maxDepth