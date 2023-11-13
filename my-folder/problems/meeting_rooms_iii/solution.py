class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        freerooms = list(range(n))
        heapify(freerooms)

        meetings.sort()
        # (endtime, roomid)
        endtimes = []
        counts = defaultdict(int)

        for start, end in meetings:
            while endtimes and endtimes[0][0] <= start:
                endedat, room = heappop(endtimes)
                heappush(freerooms, room)
            if len(freerooms) == 0:
                endedat, room = heappop(endtimes)
                heappush(freerooms, room)
                start, end = endedat, endedat+(end-start)
            
            room = heappop(freerooms)
            heappush(endtimes, (end, room))
            counts[room] += 1
        
        ans = 0
        count = counts[0]
        for room in range(1, n):
            if counts[room] > count:
                ans = room
                count = counts[room]
            elif counts[room] == count:
                ans = min(room, ans)
        
        return ans