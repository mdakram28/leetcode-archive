class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if y < x:
            x, y = y, x
        m = (y+x)//2

        # Optimization: (Single Chain) In case jumping 0 or 1 nodes, the new edge can be ignored.
        if y-x <= 1:
            return [(n-l)*2 for l in range(1, n+1)]
        
        interv = defaultdict(int)
        
        def add(start, count):
            if count <= 0: return
            interv[(start, start+count)] += 1
        
        def calc(i):
            if i < x:
                add(1, i-1)
                add(1, m-i)
                add(x-i+1, y-m)
                add(x-i+2, n-y)
            elif i <= m:
                add(1, (y-x)//2)
                add(1, (y-x)//2)
                if (y-x)%2 != 0:
                    mid = (y-x+1)//2
                    add(mid, 1)
                
                add(min(i-x+1, y-i+2), x-1)
                add(min(i-x+2, y-i+1), n-y)

        
        for i in range(1, m+1):
            calc(i)
        
        x = n-x+1
        y = n-y+1
        if y < x:
            x, y = y, x
        m = math.ceil((y+x)/2)
        for i in range(1, m):
            calc(i)

        result = []
        ends = []
        ranges = sorted(interv.keys(), reverse=True)
        total = 0
        for i in range(1, n+1):
            while ranges and ranges[-1][0] <= i:
                start, end = ranges.pop()
                c = interv[(start, end)]
                heappush(ends, (end, c))
                total += c
            while ends and ends[0][0] <= i:
                total -= heappop(ends)[1]
            result.append(total)

        return result
        