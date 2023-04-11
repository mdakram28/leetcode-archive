

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        matrix.append([0]*n)

        r = 0
        max_ar = 0
        st = []

        for r in range(m):
            matrix[r].append(0)
            st.clear()
            st.append(-1)

            # print()

            for c in range(n+1):
                if matrix[r][c] == "1":
                    matrix[r][c] = matrix[r-1][c] + 1
                else:
                    matrix[r][c] = 0
                    
                # print(f"matrix[{r}][{c}] = {matrix[r][c]}, {st=}")

                max_ar = max(
                    max_ar, 
                    matrix[r][c]
                )
                while len(st) > 1 and matrix[r][st[-1]] >= matrix[r][c]:
                    c2 = st.pop()
                    # print(f"popping {c2}, area = {(c-st[-1]-1) * matrix[r][c2]} ")
                    max_ar = max(
                        max_ar, 
                        (c-st[-1]-1) * matrix[r][c2]
                    )
                
                st.append(c)
                
            

        # print('\n'.join(map(str, matrix)))
        return max_ar

        






