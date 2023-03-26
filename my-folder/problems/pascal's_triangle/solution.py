class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(i-1):
                row.append(rows[-1][j] + rows[-1][j+1])
            row.append(1)
            rows.append(row)
        return rows