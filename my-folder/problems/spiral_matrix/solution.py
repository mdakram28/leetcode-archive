class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        size = m*n
        ret = []

        left = 0
        right = n-1
        top = 1
        bottom = m-1

        r, c  = 0, 0
        dr ,dc = 0, 1
        # print(matrix)
        for _ in range(size):
            # print(r, c, dr , dc)
            ret.append(matrix[r][c])
            if dc == 1 and c==right:
                dr, dc = 1, 0
                right -= 1
            elif dr == 1 and r==bottom:
                dr, dc = 0, -1
                bottom -= 1
            elif dc == -1 and c == left:
                dr, dc = -1, 0
                left += 1
            elif dr == -1 and r == top:
                dr, dc = 0, 1
                top += 1
            r += dr
            c += dc

        return ret
