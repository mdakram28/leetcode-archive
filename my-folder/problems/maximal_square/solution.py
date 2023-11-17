class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0]*n
        ans = 0
        for row in matrix:
            # Elements: height, index
            st = [(-float('inf'), -1)]
            # print(row)
            for i, val in enumerate(row):
                if val == "1":
                    h = heights[i] = heights[i] + 1
                else:
                    h = heights[i] = 0
                # print(i, h, st)
                while st[-1][0] >= h:
                    sqh, _ = st.pop()
                    area = min(i-st[-1][1]-1, sqh)**2
                    # print(f"area =", area)
                    ans = max(ans, area)
                st.append((h, i))
            # print([min(n-st[i-1][1]-1, st[i][0])**2 for i in range(1, len(st))])
            ans = max(ans, max(min(n-st[i-1][1]-1, st[i][0])**2 for i in range(1, len(st))))
        
        return ans