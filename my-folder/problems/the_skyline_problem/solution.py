class Solution:
    
    def getSkyline(self, b: List[List[int]]) -> List[List[int]]:
        EV_START = 1
        EV_END = -1

        events = [(l, EV_START, h) for l,r,h in b]
        events += [(r, EV_END, h) for l,r,h in b]
        events.sort()

        removed = defaultdict(int)
        q = [0]
        
        ans = []
        def boundary(x):
            while removed[q[0]] > 0:
                removed[heappop(q)] -= 1
            h = -q[0]
            if len(ans)>0 and ans[-1][0] == x:
                ans.pop()
            if len(ans)==0 or h != ans[-1][1]:
                ans.append((x, h))

        for x, ev, h in events:
            if ev == EV_START:
                heappush(q, -h)
            elif ev == EV_END:
                removed[-h] += 1
            boundary(x)
        
        return ans
            
                    