class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = float('inf')
        for i in range(1, 7):
            f1 = 0
            f2 = 0
            for a,b in zip(tops, bottoms):
                if a == i and b!=i: f2 += 1
                elif b == i and a!=i: f1 += 1
                elif a!=i and b!=i: break
            else:
                ans = min(ans, f1, f2)
        
        return -1 if ans == float('inf') else ans