
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # stationRoutes = defaultdict(list)
        # for i, r in enumerate(routes):
        #     for s in r:
        #         stationRoutes[s].append(i)
        if source == target: return 0
        n = len(routes)
        for i, r in enumerate(routes):
            routes[i] = set(r)
        
        
        # dist = defaultdict(lambda: float('inf'))
        visited = {}
        
        start = [r for r in range(n) if source in routes[r]]
        for r in start:
            visited[r] = True
        q = Deque(start)
        
        d = 0

        while q:
            d += 1
            for _ in range(len(q)):
                at = q.popleft()
                if target in routes[at]:
                    return d
                for st in routes[at]:
                    for r in range(n):
                        if st in routes[r] and r not in visited:
                            visited[r] = True
                            q.append(r)
                            

        return -1