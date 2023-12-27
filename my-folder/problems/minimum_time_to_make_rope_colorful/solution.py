class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l, r = 0, 0
        n = len(colors)
        total = 0
        while l < n:
            while r < n and colors[r] == colors[l]:
                r += 1
            # if r-l > 1:
            total += max(neededTime[l:r])
            l = r
        
        return sum(neededTime) - total

