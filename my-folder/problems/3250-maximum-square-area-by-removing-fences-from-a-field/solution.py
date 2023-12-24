class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.append(1)
        hFences.append(m)
        hFences = list(set(hFences))
        hFences.sort()
        
        vFences.append(1)
        vFences.append(n)
        vFences = list(set(vFences))
        vFences.sort()
        
        ans = 0
        vWidth = set()
        
        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                side = vFences[j]-vFences[i]
                vWidth.add(side)
        
        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                side = hFences[j]-hFences[i]
                if side in vWidth:
                    ans = max(ans, side*side)
        
        return -1 if ans == 0 else ans%(10**9+7)
                    
        
        
        
        
        
        
