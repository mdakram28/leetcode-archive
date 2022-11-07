class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for r in range(size//2):
            for c in range (r, size-r-1):
                r1, c1 = r, c
                r2, c2 = c, size-r-1
                r3, c3 = size-r-1, size-c-1
                r4, c4 = size-c-1, r
                # print(f"({r1}, {c1}) -> ({r2}, {c2})")
                # print(f"({r2}, {c2}) -> ({r3}, {c3})")
                # print(f"({r3}, {c3}) -> ({r4}, {c4})")
                # print(f"({r4}, {c4}) -> ({r1}, {c1})")
                # print("-------------------")
                matrix[r][c], matrix[c][size-r-1], matrix[size-r-1][size-c-1], matrix[size-c-1][r] = [
                    matrix[size-c-1][r], matrix[r][c], matrix[c][size-r-1], matrix[size-r-1][size-c-1]
                ]