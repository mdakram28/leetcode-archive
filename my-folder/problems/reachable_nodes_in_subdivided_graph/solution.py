class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = [[] for _ in range(n)]
        INF = float('inf')

        for n1, n2, d in edges:
            graph[n1].append((n2, d+1))
            graph[n2].append((n1, d+1))


        dist = [INF] * n
        q = [(0, 0)]
        dist[0] = 0

        while q:
            d0, at = heapq.heappop(q)
            for to, d in graph[at]:
                if (d0 + d) < dist[to]:
                    dist[to] = d0 + d
                    heapq.heappush(q, (d0+d, to))
        
        total_nodes = sum(1 if d<=maxMoves else 0 for d in dist)

        for n1, n2, d in edges:
            total_nodes += min(
                max(maxMoves-dist[n1], 0) + max(maxMoves-dist[n2], 0),
                d
            )
        return total_nodes