class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # ret = 1 if "1" in matrix[0] else (1 if "1" in (matrix[]))
        matrix[0] = [1 if r == "1" else 0 for r in matrix[0]]
        ret = 1 in matrix[0]
        for r in range(1,len(matrix)):
            matrix[r][0] = 1 if matrix[r][0] == "1" else 0
            ret = max(ret, matrix[r][0])
            for c in range(1,len(matrix[0])):
                if matrix[r][c] == "1":
                    matrix[r][c] = min(matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1]) + 1
                    ret = max(ret, matrix[r][c])
                else:
                    matrix[r][c] = 0
        # print(matrix)
        return ret*ret