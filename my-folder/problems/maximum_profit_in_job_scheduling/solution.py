class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # (end, profit)
        sl = [(0, 0)]
        for end, start, prof in sorted(zip(endTime, startTime, profit)):
            ind = bisect_right(sl, (start, float('inf')))
            prev_end, prev_prof = sl[ind-1]
            prof += prev_prof
            if sl[-1][1] >= prof:
                continue
            if sl[-1][0] == end:
                sl.pop()
            sl.append((end, prof))
        
        return sl[-1][1]
                