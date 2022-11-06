class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_v = 0
        while l < r:
            max_v = max(max_v, (r-l)*min(height[r], height[l]))
            if height[l] < height[r]:
                pl = l
                while height[l] <= height[pl] and l<r:
                    l += 1
            else:
                pr = r
                while height[r] <= height[pr] and l<r:
                    r -= 1
        return max_v