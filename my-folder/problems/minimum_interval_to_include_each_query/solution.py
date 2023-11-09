from sortedcontainers import SortedList

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        EV_ADD = 1
        EV_REM = 2
        EV_Q = 3

        events = [(l, EV_ADD, i) for i, (l, r) in enumerate(intervals)]
        events += [(r+1, EV_REM, i) for i, (l, r) in enumerate(intervals)]
        events += [(t, EV_Q, i) for i, t in enumerate(queries)]

        events.sort()
        active = []
        removed = defaultdict(int)
        ans = [0] * len(queries)

        for t, ev, i in events:
            # print(t, ev, i)
            if ev == EV_ADD:
                l, r = intervals[i]
                heappush(active, r-l+1)
            elif ev == EV_REM:
                l, r = intervals[i]
                removed[r-l+1] += 1
            else:
                while active and removed[active[0]] > 0:
                    removed[heappop(active)] -= 1
                # print(i, active, removed)
                ans[i] = active[0] if active else -1
        
        return ans