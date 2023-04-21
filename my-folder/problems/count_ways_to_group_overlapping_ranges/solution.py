class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        i = 0
        n = len(ranges)
        comp = 0
        while i < n:
            start, end = ranges[i]
            comp += 1
            # comp_start = i
            i += 1
            while i < n and ranges[i][0] <= end:
                end = max(end, ranges[i][1])
                i += 1
        return pow(2, comp, 10**9+7)