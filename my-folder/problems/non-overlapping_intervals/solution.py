from sortedcontainers import SortedList

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        ends = SortedList([(-float('inf'),0)])

        ans = 0
        for s, e in sorted(intervals, key=lambda i: i[1]):
            prev_maxint = ends[ends.bisect_left((s+1, 0))-1][1]
            ans = max(ans, 1+ prev_maxint)
            ends.add((e, ans))
        return len(intervals)-ans