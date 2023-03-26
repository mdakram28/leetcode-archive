class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        left, top = 0, 0
        right, bottom = n-1, n-1
        count = n-1

        while count > 0:
            for i in range(count):
                (
                    matrix[top][left+i], 
                    matrix[top+i][right],
                    matrix[bottom][right-i],
                    matrix[bottom-i][left]
                ) = (
                    matrix[bottom-i][left],
                    matrix[top][left+i], 
                    matrix[top+i][right],
                    matrix[bottom][right-i],
                )
            left += 1
            top += 1
            right -= 1
            bottom -= 1
            count -= 2