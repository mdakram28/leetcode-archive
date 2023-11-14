from sortedcontainers import SortedList

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        rectangles.sort(key=lambda r: r[0], reverse=True)
        mod = 10**9+7
        
        # [(end, rid)]
        active = []
        # [(y1, y2)]
        ranges = SortedList()

        def getactivesum():
            end = 0
            ret = 0
            for y1, y2 in ranges:
                if end <= y1:
                    ret = (ret+y2-y1)%mod
                    end = y2
                else:
                    ret = (ret+max(end, y2)-end)%mod
                    end = max(end, y2)
            return ret

        prevatx = 0
        total = 0

        allx = set()
        for r in rectangles:
            allx.add(r[0])
            allx.add(r[2])
        allx = sorted(list(allx))

        # print(allx)
        
        for atx in allx:
            total = (total+getactivesum()*(atx-prevatx))%mod
            # print(atx, ranges)

            # Remove all rectangles ending at or before atx
            while active and active[0][0] <= atx:
                end, r = heappop(active)
                rangeid = ranges.bisect_left(r)
                ranges.pop(rangeid)

            # add all rectangles starting at atx
            while rectangles and rectangles[-1][0] == atx:
                r = (rectangles[-1][1], rectangles[-1][3])
                heappush(active, (rectangles[-1][2], r))
                ranges.add(r)
                rectangles.pop()

            prevatx = atx
        
        # print(rectangles)
        # print(active)
        # print(ranges)

        return total