INF = float('inf')

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.dist = dist = [[INF] * n for _ in range(n)]
        
        graph = [[] for node in range(n)]
        for n1, n2, d in edges:
            graph[n1].append((n2, d))
        
        q = []
        for start in range(n):
            q.append((0, start))
            dist[start][start] = 0
            while q:
                d, at = heapq.heappop(q)
                for to, d2 in graph[at]:
                    if d+d2 < dist[start][to]:
                        dist[start][to] = d+d2
                        heapq.heappush(q, (d+d2, to))

    def addEdge(self, edge: List[int]) -> None:
        mid1, mid2, mid_dist = edge
        for n1 in range(self.n):
            for n2 in range(self.n):
                new_dist = self.dist[n1][mid1] + mid_dist + self.dist[mid2][n2]
                if new_dist < self.dist[n1][n2]:
                    self.dist[n1][n2] = new_dist
        

    def shortestPath(self, node1: int, node2: int) -> int:
        d = self.dist[node1][node2]
        return d if d != INF else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)