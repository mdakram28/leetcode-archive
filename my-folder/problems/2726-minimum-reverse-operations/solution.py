from sortedcontainers import SortedList

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        banned = set(banned)

        rempos_even = SortedList((i for i in range(0, n, 2) if i!=p and i not in banned))
        rempos_odd = SortedList((i for i in range(1, n, 2) if i!=p and i not in banned))

        dist = [-1] * n
        dist[p] = 0

        # [(d, pos)]
        q = [(0, p)]

        def get_rempos(p):
            if p%2 == 0:
                return rempos_odd if k%2 == 0 else rempos_even
            else:
                return rempos_even if k%2 == 0 else rempos_odd
        

        def can_go(a, b):
            return abs(b-a)%2 != k%2 and abs(b-a) < k

        while q:
            d, p = heappop(q)
            rempos = get_rempos(p)

            a, b = k-p-1, 2*n-k-p-1
            minright = min(a, b)
            maxright = max(a, b)
            qi = rempos.bisect_left(max(p, minright))
            while qi < len(rempos) and rempos[qi] <= maxright and can_go(p, rempos[qi]):
                newpos = rempos.pop(qi)
                heappush(q, (d+1, newpos))
                dist[newpos] = d+1
            
            a, b = k-p-1, 2*n-k-p-1
            minleft = min(a, b)
            maxleft = max(a, b)
            # print(f"{maxleft=}, {rempos=}, ")
            qi = rempos.bisect_right(min(p, maxleft))
            while qi > 0 and rempos[qi-1] >= minleft and can_go(p, rempos[qi-1]):
                newpos = rempos.pop(qi-1)
                heappush(q, (d+1, newpos))
                dist[newpos] = d+1
                qi -= 1

        return dist
