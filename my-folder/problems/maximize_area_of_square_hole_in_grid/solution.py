class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        
        top = 1
        maxh = 1
        for i in range(len(hBars)):
            if i==0 or hBars[i]-hBars[i-1] > 1:
                top = hBars[i]-1
            maxh = max(maxh, hBars[i]+1-top)
        
        left = 1
        maxw = 1
        for i in range(len(vBars)):
            if i==0 or vBars[i]-vBars[i-1] > 1:
                left = vBars[i]-1
            maxw = max(maxw, vBars[i]+1-left)
        
        return min(maxh, maxw)**2