class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        heapq.heapify(events)
        pending = []
        t = events[0][0]
        ret = 0

        while events or pending:
            while events and events[0][0] == t:
                ev = heapq.heappop(events)
                heapq.heappush(pending, ev[1])
            if pending:
                heapq.heappop(pending)
                ret += 1
            while pending and pending[0] == t:
                heapq.heappop(pending)
            
            if pending:
                t += 1
            elif events:
                t = events[0][0]
        
        return ret