class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.cum_sum = []
        m = len(matrix)
        n = len(matrix[0])
        sum_row = [0] * (n+1)
        self.cum_sum.append(sum_row)
        for row in matrix:
            sum_row = [*sum_row]
            t = 0
            for i in range(1, n+1):
                t += row[i-1]
                sum_row[i] += t
            self.cum_sum.append(sum_row)
        # print(self.cum_sum)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cum_sum[row1][col1] + self.cum_sum[row2+1][col2+1] - self.cum_sum[row1][col2+1] - self.cum_sum[row2+1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)