class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for x1, y1, x2, y2, c in specialRoads:
            graph[(x1, y1)].add(((x2, y2), c))
        
        graph[(target[0], target[1])].clear()
            
        dist = defaultdict(lambda: float('inf'))
        dist[(start[0], start[1])] = 0
        
        q = [(0, (start[0], start[1]))]
        
        while q:
            d, at = heappop(q)
            for to, d2 in graph[at]:
                if d+d2 < dist[to]:
                    dist[to] = d+d2
                    q.append((d+d2, to))
            
            for to in graph.keys():
                d2 = abs(to[1]-at[1]) + abs(to[0]-at[0])
                if d+d2 < dist[to]:
                    dist[to] = d+d2
                    q.append((d+d2, to))
            
        return dist[(target[0], target[1])]