class Solution:
    def minimumLines(self, sp: List[List[int]]) -> int:
        if len(sp) < 2:
            return 0
        sp.sort(key=lambda p: p[0])
        # print(sp)
        dy_prev = sp[1][1]-sp[0][1]
        dx_prev = sp[1][0]-sp[0][0]
        n=1
        for i in range(2, len(sp)):
            dy = sp[i][1]-sp[i-1][1]
            dx = sp[i][0]-sp[i-1][0]
            
            if dy_prev*dx != dx_prev*dy:
                n += 1
                dy_prev = dy
                dx_prev = dx
        return n