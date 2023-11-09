class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        ans = 0
        for p, peak in enumerate(maxHeights):
            total = peak
            max_h = peak
            for l in maxHeights[:p][::-1]:
                max_h = min(max_h, l)
                total += max_h
            
            max_h = peak
            for r in maxHeights[p+1:]:
                max_h = min(max_h, r)
                total += max_h
            ans = max(ans, total)
        return ans