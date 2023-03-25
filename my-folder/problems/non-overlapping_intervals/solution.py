class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        counts = [0] * (len(intervals)+1)

        def search_start(l, t):
            r = len(intervals)
            while r>l:
                mid = (l+r)//2
                if intervals[mid][0] < t:
                    l = mid+1
                else:
                    r = mid
            # print(intervals[l:], f"{t=}, {l=}, {r=}")
            return r

        max_count = 0
        for i in range(len(intervals)-1, -1, -1):
            start, end = intervals[i]
            next_idx = search_start(i+1, end)
            max_count = max(max_count, counts[next_idx] + 1)
            counts[i] = max_count
            # print(f"{i=}, {max_count=}")
        
        return len(intervals) - max_count