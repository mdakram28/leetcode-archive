class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        currEnd = float('inf')
        count = 1
        for start, end in points:
            if start > currEnd:
                count += 1
                currEnd = end
            currEnd = min(currEnd, end)
        
        return count