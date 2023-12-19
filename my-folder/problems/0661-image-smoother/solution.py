class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ret = [[0]*n for r in range(m)]

        for r in range(m):
            for c in range(n):
                vals = []
                for dr, dc in product((-1, 0, 1), repeat=2):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n:
                        vals.append(img[nr][nc])
                ret[r][c] = sum(vals)//len(vals)
        
        return ret
