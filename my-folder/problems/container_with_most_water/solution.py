class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ans = -float('inf')
        while l < r:
            # print(l, r, height[l]*(r-l))
            if height[l] <= height[r]:
                ans = max(ans, height[l]*(r-l))
                l += 1
            else:
                ans = max(ans, height[r]*(r-l))
                r -= 1
        return ans
                