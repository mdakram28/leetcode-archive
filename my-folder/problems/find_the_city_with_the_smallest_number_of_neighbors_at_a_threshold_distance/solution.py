class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        inf = float('inf')
        # dist = [inf] * n
        graph = [[] for i in range(n)]

        for n1, n2, d in edges:
            graph[n1].append((n2, d))
            graph[n2].append((n1, d))

        q = Deque()
        min_node = 0
        min_cities = inf
        
        for start in range(n):
            dist = [inf] * n
            dist[start] = 0
            q.append(start)

            while q:
                at = q.popleft()
                for to, d in graph[at]:
                    d2 = dist[at]+d
                    if d2 < dist[to] and d2 <= distanceThreshold:
                        dist[to] = d2
                        q.append(to)
            num_cities = n - dist.count(inf) - 1
            # print(start, num_cities, dist)
            if num_cities <= min_cities:
                min_node = start
                min_cities = num_cities
        
        return min_node