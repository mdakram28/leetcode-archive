class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        R = 0b001
        G = 0b010
        B = 0b100
        WHITE = 0b111
        BLACK = 0b000
        color_comp = {
            0b111: (R, G, B),
            0b110: (G, B),
            0b101: (R, B),
            0b011: (R, G),
            R: (R,),
            G: (G,),
            B: (B,),
            0b000: tuple(),
        }

        @cache
        def getways(prevcol, r, c):
            if c == n: return 1
            if r == m: return getways(prevcol, 0, c+1)
            cols = color_comp[WHITE & ~prevcol[r] & ~prevcol[r-1]]
            
            total = 0
            for col in cols:
                # print(prevcol[:r] + (col,) + prevcol[r+1:])
                total = (total + getways(
                    prevcol[:r] + (col,) + prevcol[r+1:],
                    r+1, c
                ))%(10**9+7)
            
            return total
        
        return getways((BLACK,)*(m+1), 0, 0)
