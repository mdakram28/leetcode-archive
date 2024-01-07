class Solution:
    def minMovesToCaptureTheQueen(self, A: int, B: int, C: int, D: int, E: int, F: int) -> int:
        dist = {(A, B): 0}
        q = [(0, (A, B))]
        forbidden = set([(A, B), (C, D)])
        
        def onboard(at):
            return 1 <= at[0] <= 8 and 1 <= at[1] <= 8
        
        while q:
            _, at = heappop(q)
            r, c = at
            # print(at)
            for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
                d2 = dist[at] + 1
                for diff in range(1, 9):
                    to = r+diff*dr, c+diff*dc
                    if to in forbidden:
                        d2 += 1
                    if onboard(to) and d2 < dist.get(to, float('inf')):
                        dist[to] = d2
                        heappush(q, (d2, to))
                    
        
        # for r in range(1, 9):
        #     for c in range(1, 9):
        #         at = (r, c)
        #         print(dist.get(at, 'x'), end='')
        #     print()
        # print()
        
        
        rook = dist[(E, F)]
        
        dist = {(C, D): 0}
        q = [(0, (C, D))]
        while q:
            _, at = heappop(q)
            r, c = at
            for dr, dc in (1, 1), (1, -1), (-1, 1), (-1, -1):
                d2 = dist[at] + 1
                for diff in range(1, 9):
                    to = r+diff*dr, c+diff*dc
                    if to in forbidden:
                        d2 += 1
                    if onboard(to) and d2 < dist.get(to, float('inf')):
                        dist[to] = d2
                        heappush(q, (d2, to))
                   
        
        # for r in range(1, 9):
        #     for c in range(1, 9):
        #         at = (r, c)
        #         print(dist.get(at, 'x'), end='')
        #     print()
        # print()
        
        bishop = dist.get((E,F), float('inf'))
        
        return min(rook, bishop)