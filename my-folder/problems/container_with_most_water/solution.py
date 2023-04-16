class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        r = n-1
        max_a = 0
        for l, h in enumerate(height):
            while r>l and height[r] <= h:
                max_a = max(max_a, height[r]*(r-l))
                r -= 1
            if r <= l:
                break
            max_a = max(max_a, h*(r-l))
        return max_a
