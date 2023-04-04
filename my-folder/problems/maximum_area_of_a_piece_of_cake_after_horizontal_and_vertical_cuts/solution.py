class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_h = 0
        prev = 0
        for n in horizontalCuts:
            max_h = max(max_h, n-prev)
            prev = n
        max_h = max(max_h, h-prev)


        max_w = 0
        prev = 0
        for n in verticalCuts:
            max_w = max(max_w, n-prev)
            prev = n
        max_w = max(max_w, w-prev)
        mod = 10**9 + 7
        return (max_w*max_h)%mod